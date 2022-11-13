from django.shortcuts import render

def index(request):
    value = 'Hello Python'
    return render(request, 'index.html', locals())
