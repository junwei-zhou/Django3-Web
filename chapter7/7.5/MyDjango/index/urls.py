from django.urls import path
from .views import *

urlpatterns = [
    # 定义路由
    path('', indexView, name='index'),
]
