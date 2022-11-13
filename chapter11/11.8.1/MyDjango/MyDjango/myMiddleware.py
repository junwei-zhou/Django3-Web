from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        """运行Django将自动执行"""
        self.get_response = get_response
        print('This is __init__')

    def process_request(self, request):
        """生成请求对象后，路由匹配之前"""
        print('This is process_request')

    def process_view(self, request, func, args, kwargs):
        """路由匹配后，视图函数调用之前"""
        print('This is process_view')

    def process_exception(self, request, exception):
        """视图函数发生异常时"""
        print('This is process_exception')

    def process_response(self, request, response):
        """视图函数执行后，响应内容返回浏览器之前"""
        print('This is process_response')
        return response