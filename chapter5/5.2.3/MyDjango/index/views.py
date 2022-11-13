from django.views.generic.edit import UpdateView
from .models import PersonInfo
from django.http import HttpResponse

def result(request):
    return HttpResponse('Success')

class index(UpdateView):
    template_name = 'index.html'
    success_url = '/result'
    model = PersonInfo
    # fields设置模型字段，从而生成表单字段
    fields = ['name', 'age']
    slug_url_kwarg = 'age'
    slug_field = 'age'
    context_object_name = 'personinfo'
    extra_context = {'title': '人员信息表'}
