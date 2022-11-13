
from django.urls import path
from .views import *

urlpatterns = [
    # 用户注册界面的路由地址，显示微博登录链接。
    path('', loginView, name='login'),
    # 注册后回调的页面，成功注册后跳转回站内地址。
    path('success', success, name='success')
]
