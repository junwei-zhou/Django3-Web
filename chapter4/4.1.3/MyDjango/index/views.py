from django.shortcuts import render
from django.http import Http404


def index(request):
    if request.GET.get('error', ''):
        raise Http404("page does not exist")
    else:
        return render(request, 'index.html')


def pag_not_found(request):
    """全局404的配置函数 """
    return render(request, '404.html', status=404)


def page_error(request):
    """全局500的配置函数 """
    return render(request, '500.html', status=500)
