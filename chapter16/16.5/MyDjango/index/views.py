from django.http import HttpResponse

def checkView(request):
    return HttpResponse('success')

def indexView(request):
    return HttpResponse('This is Index')

def userView(request):
    return HttpResponse('This is User')