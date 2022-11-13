from django.shortcuts import render
from django.http import HttpResponse
# 用户注册页面
def loginView(request):
    title = '用户注册'
    return render(request, 'user.html', locals())

# 注册后回调的页面
def success(request):
    return HttpResponse('注册成功')