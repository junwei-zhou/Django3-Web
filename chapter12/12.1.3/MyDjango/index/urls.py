
from django.urls import path
from .views import *
urlpatterns = [
    # 视图函数
    path('', vocationDef, name='myDef'),
    # 视图类
    path('myClass/', vocationClass.as_view(), name='myClass'),
]
