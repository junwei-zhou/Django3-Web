from django.views.generic.edit import FormView
from .form import PersonInfoForm
from django.http import HttpResponse

def result(request):
    return HttpResponse('Success')

class index(FormView):
    initial = {'name': 'Betty', 'age': 20}
    template_name = 'index.html'
    success_url = '/result'
    form_class = PersonInfoForm
    extra_context = {'title': '人员信息表'}
