
from django.urls import path
from .views import *

urlpatterns = [
    # 用户注册
    path('', registerView, name='register'),
    # 用户登录
    path('login.html', loginView, name='login'),
    # 用户注销
    path('logout.html', logoutView, name='logout'),
    # 用户信息
    path('info.html', infoView, name='info')
]
