from django.urls import path
from .views import *

urlpatterns = [
    # 定义路由
    path('create/', creatView, name='create'),
    path('cancel/', cancelView, name='cancel'),
]
