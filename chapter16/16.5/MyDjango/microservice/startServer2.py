from microservice.startServer import *


if __name__ == '__main__':
    server = HttpServer('127.0.0.1', 8001, '127.0.0.1', 8500, DjangoServer)
    server.startServer()
