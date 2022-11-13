
from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    # 指向index的路由文件urls.py
    path('', include(('index.urls', 'index'), namespace='index')),
]