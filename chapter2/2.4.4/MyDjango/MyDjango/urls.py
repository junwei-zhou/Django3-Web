from django.contrib import admin
from django.urls import path
# 导入项目应用index
from index.views import indexView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView, name='index')
]
