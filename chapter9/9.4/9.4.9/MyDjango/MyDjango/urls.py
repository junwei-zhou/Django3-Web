
from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    # 指向index的路由文件urls.py
    path('admin/', admin.site.urls),
    path('', include(('index.urls', 'index'), namespace='index')),
]


