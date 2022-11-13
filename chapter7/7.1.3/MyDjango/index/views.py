from django.http import HttpResponse
from .models import PersonInfo

def index(request):
    return HttpResponse('aa')
