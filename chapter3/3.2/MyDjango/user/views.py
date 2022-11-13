from django.http import HttpResponse
def index(request):
    return HttpResponse('This is userIndex')

def userLogin(request):
    return HttpResponse('This is userLogin')