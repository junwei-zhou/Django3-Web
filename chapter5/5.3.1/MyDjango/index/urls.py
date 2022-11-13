from django.urls import path
from .views import *

urlpatterns = [
    # 定义路由
    path('<int:year>/<int:month>.html', index.as_view(), name='index'),
    # path('<int:year>/<str:month>.html', index.as_view(), name='index'),
]
