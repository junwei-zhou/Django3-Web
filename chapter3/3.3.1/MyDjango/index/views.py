from django.http import HttpResponse
from django.shortcuts import render
def mydate(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))

def index(request):
    return render(request, 'index.html')
