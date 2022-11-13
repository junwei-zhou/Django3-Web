from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     html = '<h1>Hello World</h1>'
#     return HttpResponse(html, status=200)

# def index(request):
#     value = {'title': 'Hello MyDjango'}
#     return render(request, 'index.html', context=value)

def index(request):
    title = {'key': 'Hello MyDjango'}
    content = {'key': 'This is MyDjango'}
    return render(request, 'index.html', locals())