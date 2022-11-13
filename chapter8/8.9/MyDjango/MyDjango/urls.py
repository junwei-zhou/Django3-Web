from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    # 指向index的路由文件urls.py
    path('', include(('index.urls', 'index'), namespace='index')),
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
]