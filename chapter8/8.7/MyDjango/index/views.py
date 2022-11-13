from django.shortcuts import render
from django.http import HttpResponse
from .form import *
def indexView(request):
    # GET请求
    if request.method == 'GET':
        v = VocationForm(prefix='vv')
        return render(request, 'index.html', locals())
    # POST请求
    else:
        # 由于在GET请求设置了参数prefix
        # 实例化时必须设置参数prefix，否则无法获取POST的数据
        v = VocationForm(data=request.POST, prefix='vv')
        # 判断当前请求来自哪一个按钮
        if 'add' in request.POST:
            return HttpResponse('提交成功')
        else:
            return HttpResponse('修改成功')