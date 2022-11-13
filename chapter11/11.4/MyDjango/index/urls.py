
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('success', success, name='success'),
    path('iClass', iClass.as_view(), name='iClass'),
]
