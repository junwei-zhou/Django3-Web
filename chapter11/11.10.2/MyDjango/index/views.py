from django.http import HttpResponse
from MyDjango.sg import my_signals

def index(request):
    # 使用自定义信号
    print('已连接信号')
    my_signals.send(sender='MySignals', name='xyh', age=18)
    return HttpResponse('请求成功')