from django.urls import path
from . import views

urlpatterns = [
    # 定义首页的路由
    path('', views.index, name='index'),
    # 定义商城的路由
    path('shop', views.shop, name='shop')
]
