import consul
from random import randint
import requests
import json


class ConsulClient():
    '''定义consul操作类'''
    def __init__(self, host=None, port=None, token=None):
        '''初始化，指定consul主机、端口和token'''
        self.host = host  # consul 主机
        self.port = port  # consul 端口
        self.token = token
        self.consul = consul.Consul(host=host, port=port)

    def register(self, name, service_id, address, port, tags, interval, url):
        '''注册服务'''
        # 设置检测模式：http和tcp
        # tcp模式
        # check=consul.Check().tcp(self.host, self.port,
        # "5s", "30s", "30s")
        # http模式
        check = consul.Check().http(url, interval,
                                    timeout=None,
                                    deregister=None,
                                    header=None)
        self.consul.agent.service.register(name,
                                           service_id=service_id,
                                           address=address,
                                           port=port,
                                           tags=tags,
                                           interval=interval,
                                           check=check)

    def getService(self, name):
        '''通过负载均衡获取服务实例'''
        # 获取相应服务下的DataCenter
        url = 'http://' + self.host + ':' + str(self.port) + '/v1/catalog/service/' + name
        dataCenterResp = requests.get(url)
        if dataCenterResp.status_code != 200:
            raise Exception('can not connect to consul ')
        listData = json.loads(dataCenterResp.text)
        # 初始化DataCenter
        dcset = set()
        for service in listData:
            dcset.add(service.get('Datacenter'))
        # 服务列表初始化
        serviceList = []
        for dc in dcset:
            if self.token:
                url = f'http://{self.host}:{self.port}/v1/health/service/{name}?dc={dc}&token={self.token}'
            else:
                url = f'http://{self.host}:{self.port}/v1/health/service/{name}?dc={dc}&token='
            resp = requests.get(url)
            if resp.status_code != 200:
                raise Exception('can not connect to consul ')
            text = resp.text
            serviceListData = json.loads(text)

            for serv in serviceListData:
                status = serv.get('Checks')[1].get('Status')
                # 选取成功的节点
                if status == 'passing':
                    address = serv.get('Service').get('Address')
                    port = serv.get('Service').get('Port')
                    serviceList.append({'port': port, 'address': address})
        if len(serviceList) == 0:
            raise Exception('no serveice can be used')
        else:
            # 随机获取一个可用的服务实例
            print('当前服务列表：', serviceList)
            service = serviceList[randint(0, len(serviceList) - 1)]
            return service['address'], int(service['port'])
