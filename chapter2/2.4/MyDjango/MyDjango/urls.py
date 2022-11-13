
from django.contrib import admin
from django.urls import path
# 导入项目应用index
from index.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
]
