from django.shortcuts import render
from django.http import HttpResponse
from .form import *
from .models import *
def indexView(request):
    # 参数extra是设置表单数量
    # 参数max_num是限制表单的最大数量
    pfs = forms.formset_factory(PersonInfoForm, extra=2, max_num=5)

    # modelformset_factory是在formset_factory基础上加入模型操作功能
    # 它是将模型当前数据以表单形式展示，可用于删除、排序等操作
    # pfs = forms.modelformset_factory(model=PersonInfo, form=PersonInfoForm, extra=0, max_num=5)

    # GET请求
    if request.method == 'GET':
        p = pfs()
        return render(request, 'index.html', locals())
    # POST请求
    else:
        p = pfs(request.POST)
        if p.is_valid():
            for i in p:
                i.save()
            return HttpResponse('新增成功')
        else:
            # 获取错误信息，并以json格式输出
            error_msg = p.errors.as_json()
            print(error_msg)
            return render(request, 'index.html', locals())