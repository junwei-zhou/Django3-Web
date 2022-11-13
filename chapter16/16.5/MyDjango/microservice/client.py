from microservice.consulclient import ConsulClient
import requests

class HttpClient():
    '''
    从Consul获取服务的响应内容
    首先从数据中心获取已注册的服务实例，
    得到服务实例的API接口，
    再向API接口发送HTTP请求，获取服务的响应内容。
    '''
    def __init__(self, consulhost, consulport, appname):
        self.appname = appname
        self.cc = ConsulClient(host=consulhost, port=consulport)

    def request(self):
        '''
        向Consul发送HTTP请求，获取服务实例
        再向服务实例发送HTTP请求，获取响应内容
        '''
        # 调用getService()方法从数据中心随机获取服务实例
        host, port = self.cc.getService(self.appname)
        print('选中的服务实例为：', host, port)
        # 向服务实例发送HTTP请求
        url = f'http://{host}:{port}/{self.appname}'
        scrapyMessage = requests.get(url).text
        print(scrapyMessage)

if __name__ == '__main__':
    client = HttpClient('127.0.0.1', '8500', 'index')
    client.request()
    client = HttpClient('127.0.0.1', '8500', 'user')
    client.request()