from django.shortcuts import render
from django.http import HttpResponse
from .form import *
from .models import *
def index(request):
    # GET请求
    if request.method == 'GET':
        id = request.GET.get('id', '')
        if id:
            d = Vocation.objects.filter(id=id).values()
            d = list(d)[0]
            d['person'] = d['person_id']
            i = dict(initial=d, label_suffix='*', prefix='vv')
            # 将参数i传入表单VocationForm执行实例化
            v = VocationForm(**i)
        else:
            v = VocationForm(prefix='vv')
        return render(request, 'index.html', locals())
    # POST请求
    else:
        # 由于在GET请求设置了参数prefix
        # 实例化时必须设置参数prefix，否则无法获取POST的数据
        v = VocationForm(data=request.POST, prefix='vv')
        if v.is_valid():
            # 获取网页控件name的数据
            # 方法一
            title = v['title']
            # 方法二
            # cleaned_data将控件name的数据进行清洗
            ctitle = v.cleaned_data['title']
            print(ctitle)
            # 将数据更新到模型Vocation
            id = request.GET.get('id', '')
            d = v.cleaned_data
            d['person_id'] = int(d['person'])
            Vocation.objects.filter(id=id).update(**d)
            return HttpResponse('提交成功')
        else:
            # 获取错误信息，并以json格式输出
            error_msg = v.errors.as_json()
            print(error_msg)
            return render(request, 'index.html', locals())