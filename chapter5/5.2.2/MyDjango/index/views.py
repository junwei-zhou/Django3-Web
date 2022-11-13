from django.views.generic.edit import CreateView
from .form import PersonInfoForm
from .models import PersonInfo
from django.http import HttpResponse

def result(request):
    return HttpResponse('Success')

class index(CreateView):
    initial = {'name': 'Betty', 'age': 20}
    template_name = 'index.html'
    success_url = '/result'
    # 表单生成方式一
    # form_class = PersonInfoForm
    # 表单生成方式二
    model = PersonInfo
    # fields设置模型字段，从而生成表单字段
    fields = ['name', 'age']
    extra_context = {'title': '人员信息表'}
