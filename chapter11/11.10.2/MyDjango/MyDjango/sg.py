# 自定义信号
from index.models import PersonInfo
from django.dispatch import Signal


my_signals = Signal()
# 注册信号的回调函数
def mySignal(sender, **kwargs):
    print('sender is ', sender)
    print('kwargs is ', kwargs)
    print(PersonInfo.objects.all())
# 将自定义的信号my_signals与回调函数mySignal绑定
my_signals.connect(mySignal)
# 如果一个信号有多个回调函数，可以通过connect()和disconnect()进行切换
# my_signals.disconnect(mySignal)

