
from django.urls import path
from .views import *
urlpatterns = [
    # 用户登录界面
    path('', loginView, name='login'),
    # 验证码验证API接口
    path('ajax_val', ajax_val, name='ajax_val')
]
