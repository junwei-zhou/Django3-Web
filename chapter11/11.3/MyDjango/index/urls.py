
from django.urls import path
from . import views

urlpatterns = [
    # 网站首页
    path('', views.index, name='index'),
]
