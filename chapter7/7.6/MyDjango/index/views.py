from django.shortcuts import render
from .models import *

def indexView(request):
    personInfo = PersonInfo.objects.all()
    return render(request, 'index.html', locals())
