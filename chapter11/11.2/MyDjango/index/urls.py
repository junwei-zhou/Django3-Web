
from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    # 网站首页设置路由缓存
    # path('', cache_page(timeout=10, cache='MyDjango', key_prefix='MyURL')(views.index), name='index'),
    path('', views.index, name='index'),
]
