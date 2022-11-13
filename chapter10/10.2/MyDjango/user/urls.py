
from django.urls import path
from .views import *

urlpatterns = [
    path('', findpsView, name='findps'),
]
