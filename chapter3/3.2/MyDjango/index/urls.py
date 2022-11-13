from django.urls import re_path, path
from . import views
urlpatterns = [
    re_path('(?P<year>[0-9]{4}).html', views.mydate, name='mydate'),
    path('', views.index, name='index')
]

