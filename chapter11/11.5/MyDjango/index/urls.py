
from django.urls import path
from .views import *

urlpatterns = [
    path('<page>/', index, name='index'),
]
