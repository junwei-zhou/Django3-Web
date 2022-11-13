
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('api/', indexApi, name='indexApi'),
]
