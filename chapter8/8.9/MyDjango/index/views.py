from django.shortcuts import render
from django.http import HttpResponse
from .form import PersonInfoForm
from .models import PersonInfo, CertificateInfo
from django.conf import settings
import os

def indexView(request):
    # GET请求
    if request.method == 'GET':
        id = request.GET.get('id', '')
        if id:
            i = PersonInfo.objects.filter(id=id).first()
            p = PersonInfoForm(instance=i)
        else:
            p = PersonInfoForm()
        return render(request, 'index.html', locals())
    # POST请求
    else:
        p = PersonInfoForm(data=request.POST, files=request.FILES)
        if p.is_valid():
            name = p.cleaned_data['name']
            result = PersonInfo.objects.filter(name=name)
            # 数据不存在，则新增数据
            if not result:
                p = p.save()
                id = p.id
                # 遍历上存的文件，依次添加证件信息
                # 如果网页有多个文件上存控件
                # 可以通过getlist方法获取指定的文件上存控件
                for f in request.FILES.getlist('certificate'):
                    # 修改文件名
                    # 如果不同用户上存相同文件名的文件
                    # 防止media文件夹会覆盖文件
                    f.name = f'{id}.'.join(f.name.split('.'))
                    d = dict(person_id=id, certificate=f)
                    CertificateInfo.objects.create(**d)
                return HttpResponse('新增成功')
            # 数据存在，则修改数据
            else:
                age = p.cleaned_data['age']
                d = dict(name=name, age=age)
                result.update(**d)
                # 删除旧的证件
                id = result.first().id
                # 删除media文件夹的文件，然后删除数据表的数据
                for c in CertificateInfo.objects.filter(person_id=id):
                    # c.certificate是文件对象，通过name属性获取文件名
                    # 删除media文件夹的文件
                    fn = c.certificate.name
                    os.remove(os.path.join(settings.MEDIA_ROOT, fn))
                    # 删除数据表的数据
                    c.delete()
                # 添加新的证件
                for f in request.FILES.getlist('certificate'):
                    # 修改文件名
                    # 如果不同用户上存相同文件名的文件
                    # 防止media文件夹会覆盖文件
                    f.name = f'{id}.'.join(f.name.split('.'))
                    d = dict(person_id=id, certificate=f)
                    CertificateInfo.objects.create(**d)
                return HttpResponse('修改成功')
        else:
            # 获取错误信息，并以json格式输出
            error_msg = p.errors.as_json()
            print(error_msg)
            return render(request, 'index.html', locals())