
from django.urls import path
from .views import synView, asynView

urlpatterns = [
    path('syn', synView, name='syn'),
    path('asyn', asynView, name='asyn'),
]
