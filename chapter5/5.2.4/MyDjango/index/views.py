from django.views.generic.edit import DeleteView
from .models import PersonInfo
from django.http import HttpResponse

def result(request):
    return HttpResponse('Success')

class index(DeleteView):
    template_name = 'index.html'
    success_url = '/result'
    model = PersonInfo
    context_object_name = 'personinfo'
    extra_context = {'title': '人员信息表'}
