# 以8.4章节的例子为例
from django.shortcuts import render
from django.http import HttpResponse
from .form import *
def indexView(request):
    # GET请求
    if request.method == 'GET':
        v = VocationForm(prefix='vv')
        w = VocationForm(prefix='ww')
        return render(request, 'index.html', locals())
    # POST请求
    else:
        # 由于在GET请求设置了参数prefix
        # 实例化时必须设置参数prefix，否则无法获取POST的数据
        v = VocationForm(data=request.POST, prefix='vv')
        w = VocationForm(data=request.POST, prefix='ww')
        if v.is_valid():
            print(v.data)
            return HttpResponse('表单1提交成功')
        elif w.is_valid():
            print(w.data)
            return HttpResponse('表单2提交成功')
        else:
            # 获取错误信息，并以json格式输出
            error_msg = v.errors.as_json()
            print(error_msg)
            return render(request, 'index.html', locals())