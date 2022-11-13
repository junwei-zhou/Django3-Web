from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now
from django.shortcuts import Http404


class MyMiddleware(MiddlewareMixin):
    def process_view(self, request, func, args, kwargs):
        if func.__name__ != 'index':
            salt = request.COOKIES.get('value', '')
            try:
                request.get_signed_cookie('MySign', salt=salt)
            except Exception as e:
                print(e)
                raise Http404('当前Cookie无效哦！')

    def process_response(self, request, response):
        salt = str(now())
        response.set_signed_cookie(
            'MySign',
            'sign',
            salt=salt,
            max_age=10
        )
        response.set_cookie('value', salt)
        return response
