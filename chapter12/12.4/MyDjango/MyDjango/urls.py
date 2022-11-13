
from django.urls import path, include
urlpatterns = [
    path('', include(('user.urls', 'user'), namespace='user')),
    # 导入social_django的路由信息
    path('', include('social_django.urls', namespace='social'))
]