from django.urls import path
from .views import *

urlpatterns = [
    # 定义路由
    path('<pk>/<age>.html', index.as_view(), name='index'),
]
