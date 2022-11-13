from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# API接口判断请求头
def getHeader(request):
    header = request.META.get('HTTP_SIGN', '')
    if header:
        value = {'header': header}
    else:
        value = {'header': 'null'}
    return JsonResponse(value)
