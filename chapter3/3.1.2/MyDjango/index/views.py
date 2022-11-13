from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')

def new(request):
    return HttpResponse('This is new page')