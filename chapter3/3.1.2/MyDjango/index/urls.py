from django.conf.urls import url
from . import views
urlpatterns = [
    url('^$', views.index),
    url('^new/$', views.new)
]