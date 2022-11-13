from django.http import HttpResponse
from django.shortcuts import render
def mydate(request, year):
    return HttpResponse(str(year))

def index(request):
    return render(request, 'index.html')