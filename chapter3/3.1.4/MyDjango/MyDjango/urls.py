
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    # 指向内置admin系统的路由文件sites.py
    path('admin/', admin.site.urls),
    # 指向index的路由文件urls.py
    path('', include('index.urls')),
]
