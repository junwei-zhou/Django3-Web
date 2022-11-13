from django.urls import path
from .views import *

urlpatterns = [
    # 定义路由index
    path('', indexView, name='index'),
]
