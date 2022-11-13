from django.urls import path
from .views import *

urlpatterns = [
    # 定义路由
    path('', index, name='index'),
    path('turnTo', turnTo.as_view(), name='turnTo')
]
