from django.core.signals import request_finished
from django.core.signals import request_started
from django.core.signals import got_request_exception

from django.db.models.signals import class_prepared
from django.db.models.signals import pre_init, post_init
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import pre_delete, post_delete
from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_migrate, post_migrate

from django.test.signals import setting_changed
from django.test.signals import template_rendered
from django.db.backends.signals import connection_created

# 编写方法1：
# 设置内置信号request_started的回调函数signal_request
def signal_request(sender, **kwargs):
    print("request is coming")
    print(sender)
    print(kwargs)
# 将内置信号request_started与回调函数signal_request绑定
request_started.connect(signal_request)



# 编写方法2：
from django.dispatch import receiver
# 使用内置函数receiver作为回调函数的装饰器
# 将内置信号request_started与回调函数signal_request_2绑定
@receiver(request_started)
# 设置内置信号request_started的回调函数signal_request
def signal_request_2(sender, **kwargs):
    print("request is coming too")
    print(sender)
    print(kwargs)


