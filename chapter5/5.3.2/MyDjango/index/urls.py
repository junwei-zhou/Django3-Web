from django.urls import path
from .views import *

urlpatterns = [
    # 定义路由
    path('<int:year>/<int:week>.html', index.as_view(), name='index'),
]
