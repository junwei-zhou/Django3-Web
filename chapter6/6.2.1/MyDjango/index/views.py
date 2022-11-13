from django.shortcuts import render

def index(request):
    value = {'name': 'This is Jinja2'}
    return render(request, 'index.html', locals())
