from django.urls import path
from . import views

urlpatterns = [
    # 定义路由
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('myCookie', views.myCookie, name='myCookie'),
]
