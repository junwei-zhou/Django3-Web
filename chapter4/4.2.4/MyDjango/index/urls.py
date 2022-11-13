from django.urls import path
from . import views

urlpatterns = [
    # 定义路由
    path('', views.index, name='index'),
    path('getHeader', views.getHeader, name='getHeader')
]
