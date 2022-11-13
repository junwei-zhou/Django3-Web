from django.http import HttpResponse
from django.shortcuts import reverse
from django.urls import resolve

def mydate(request, year, month, day):
    args = ['2019', '12', '12']
    result = resolve(reverse('index:mydate', args=args))
    print('kwargs：', result.kwargs)
    print('url_name：', result.url_name)
    print('namespace：', result.namespace)
    print('view_name：', result.view_name)
    print('app_name：', result.app_name)
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))

def index(request):
    kwargs = {'year': 2010, 'month': 2, 'day': 10}
    args = ['2019', '12', '12']
    print(reverse('index:mydate', args=args))
    print(reverse('index:mydate', kwargs=kwargs))
    return HttpResponse(reverse('index:mydate', args=args))
