
from django.contrib import admin
from django.conf.urls import url
from django.urls import include
urlpatterns = [
    # 指向内置admin系统的路由文件sites.py
    url('admin/', admin.site.urls),
    # 指向index的路由文件urls.py
    url('^', include('index.urls')),
]
