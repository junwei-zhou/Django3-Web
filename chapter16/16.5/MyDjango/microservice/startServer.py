from microservice.consulclient import ConsulClient
import os

class DjangoServer():
    '''自定义Django的启动方式'''
    def __init__(self, host, port):
        self.host = host
        self.port = port
        # appname代表微服务的API地址
        self.appname = ['index', 'user']

    def run(self):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'MyDjango.settings')
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
            ) from exc
        filePath = os.getcwd() + '\\' + os.path.basename(__file__)
        hostAndPort = f'{self.host}:{self.port}'
        execute_from_command_line([filePath, 'runserver', hostAndPort])

class HttpServer():
    '''定义服务注册与发现，将Django服务注册到Consul中'''
    def __init__(self, host, port, consulhost, consulport, appClass):
        self.port = port
        self.host = host
        self.app = appClass(host=host, port=port)
        self.appname = self.app.appname
        self.consulhost = consulhost
        self.consulport = consulport

    def startServer(self):
        client = ConsulClient(host=self.consulhost, port=self.consulport)
        # 注册服务，将路由index和user依次注册
        for aps in self.appname:
            service_id = aps + self.host + ':' + str(self.port)
            url = f'http://{self.host}:{str(self.port)}/check'
            client.register(aps, service_id=service_id, address=self.host,
                            port=self.port, tags=['master'],
                            interval='30s', url=url)
        # 启动Django
        self.app.run()

if __name__ == '__main__':
    server = HttpServer('127.0.0.1', 8000, '127.0.0.1', 8500, DjangoServer)
    server.startServer()

















