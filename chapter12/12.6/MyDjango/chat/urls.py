from django.urls import path
from .views import *

urlpatterns = [
    # 用于开启新的聊天室
    path('', newChat, name='newChat'),
    # 创建聊天室
    path('<room_name>/', room, name='room'),
]
