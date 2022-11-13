from django.urls import path
from .views import *

urlpatterns = [
    # 定义路由
    path('<age>.html', index.as_view(), name='index'),
    path('result', result, name='result')
]
