from django.shortcuts import render
from django.http import HttpResponse
from .form import *
from .models import *
def index(request):
    # GET请求
    if request.method == 'GET':
        id = request.GET.get('id', '')
        if id:
            i = Vocation.objects.filter(id=id).first()
            # 将参数i传入表单VocationForm执行实例化
            v = VocationForm(instance=i, prefix='vv')
        else:
            v = VocationForm(prefix='vv')
        return render(request, 'index.html', locals())
    # POST请求
    else:
        # 由于在GET请求设置了参数prefix
        # 实例化时设置参数prefix，否则无法获取POST的数据
        v = VocationForm(data=request.POST, prefix='vv')
        # is_valid()会使字段payment自增加10
        if v.is_valid():
            # 根据请求参数id查询模型数据是否存在
            id = request.GET.get('id')
            result = Vocation.objects.filter(id=id)
            # 数据不存在，则新增数据
            if not result:
                # 数据保存方法一
                # 直接将数据保存到数据库
                # v.save()
                # 数据保存方法二
                # 将save的参数commit=False
                # 生成数据库对象v1，修改v1的属性值并保存
                v1 = v.save(commit=False)
                v1.title = '初级' + v1.title
                v1.save()
                # 数据保存方法三
                # save_m2m()方法用于保存ManyToMany的数据模型
                # v.save_m2m()
                return HttpResponse('新增成功')
            # 数据存在，则修改数据
            else:
                d = v.cleaned_data
                d['title'] = '中级' + d['title']
                result.update(**d)
                return HttpResponse('修改成功')
        else:
            # 获取错误信息，并以json格式输出
            error_msg = v.errors.as_json()
            print(error_msg)
            return render(request, 'index.html', locals())