from django.http import HttpResponse
# 在视图中必须导入sg文件，否则信号机制不会生效
from MyDjango.sg import *

def index(request):
    print('This is view')
    return HttpResponse('请求成功')