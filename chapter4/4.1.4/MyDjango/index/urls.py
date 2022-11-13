from django.urls import path
from . import views

urlpatterns = [
    # 定义首页的路由
    path('', views.index, name='index'),
    path('download/file1', views.download1, name='download1'),
    path('download/file2', views.download2, name='download2'),
    path('download/file3', views.download3, name='download3'),
]
