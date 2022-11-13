
from django.urls import path, include
from .consumers import ChatConsumer

urlpatterns = [
    path('', include(('chat.urls', 'chat'), namespace='chat'))
]

websocket_urlpatterns = [
    # 使用同步方式实现
    # path('ws/chat/<room_name>/', ChatConsumer),
    # 如果使用异步方式实现，路由的视图必须调用as_asgi()
    path('ws/chat/<room_name>/', ChatConsumer.as_asgi()),
]
