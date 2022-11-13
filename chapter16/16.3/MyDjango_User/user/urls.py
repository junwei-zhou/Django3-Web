
from django.urls import path
from .views import *
urlpatterns = [
    path('', userView, name='user'),
]
