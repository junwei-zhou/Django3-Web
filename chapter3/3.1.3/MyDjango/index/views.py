from django.http import HttpResponse
def myvariable(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))

def index(request, month):
    return HttpResponse('这是路由地址信息之外的变量：' + month)
