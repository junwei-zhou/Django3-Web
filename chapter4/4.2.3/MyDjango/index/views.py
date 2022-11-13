from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import reverse

def index(request):
    return render(request, 'index.html')

def create(request):
    r = redirect(reverse('index:index'))
    # 添加Cookie
    # response.set_cookie('uid', 'Cookie_Value')
    r.set_signed_cookie('uuid', 'id', salt='MyDj', max_age=10)
    return r

def myCookie(request):
    cookieExist = request.COOKIES.get('uuid', '')
    if cookieExist:
        # 验证加密后的Cookies是否有效
        try:
            request.get_signed_cookie('uuid', salt='MyDj')
        except:
            raise Http404('当前Cookie无效哦！')
        return HttpResponse('当前Cookie为：' + cookieExist)
    else:
        raise Http404('当前访问没有Cookie哦！')

