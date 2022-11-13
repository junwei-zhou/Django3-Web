from django.shortcuts import render
from django.http import HttpResponse
from .form import *
def index(request):
    # GET请求
    if request.method == 'GET':
        v = VocationForm()
        return render(request, 'index.html', locals())
    # POST请求
    else:
        v = VocationForm(request.POST)
        if v.is_valid():
            # 获取网页控件name的数据
            # 方法一
            title = v['title']
            # 方法二
            # cleaned_data将控件name的数据进行清洗
            ctitle = v.cleaned_data['title']
            return HttpResponse('提交成功')
        else:
            # 获取错误信息，并以json格式输出
            error_msg = v.errors.as_json()
            print(error_msg)
            return render(request, 'index.html', locals())

