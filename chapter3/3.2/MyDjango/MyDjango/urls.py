
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    # 指向内置admin系统的路由文件sites.py
    path('admin/', admin.site.urls),
    # 指向index的路由文件urls.py
    path('', include(('index.urls', 'index'), namespace='index')),
    # 指向user的路由文件urls.py
    path('user/', include(('user.urls', 'user'), namespace='user'))
]
