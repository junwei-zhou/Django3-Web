from django.shortcuts import render
from .form import *

def index(request):
    v = VocationForm()
    return render(request, 'index.html', locals())

