
from django.urls import path
from .views import *
urlpatterns = [
    path('', apiView, name='api'),
]
