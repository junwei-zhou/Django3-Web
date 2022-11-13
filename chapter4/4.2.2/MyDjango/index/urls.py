from django.urls import path
from . import views

urlpatterns = [
    # 定义路由
    path('', views.upload, name='uploaded'),
]
