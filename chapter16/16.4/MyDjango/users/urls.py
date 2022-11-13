from django.urls import path
from .views import userView, getView
urlpatterns = [
    path('users/', userView, name='users'),
    path('userInfo/', getView, name='getUser'),
]