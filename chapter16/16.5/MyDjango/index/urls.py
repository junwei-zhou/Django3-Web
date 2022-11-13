from django.urls import path
from .views import *

urlpatterns = [
    path('check/', checkView, name='check'),
    path('index/', indexView, name='index'),
    path('user/', userView, name='user'),
]
