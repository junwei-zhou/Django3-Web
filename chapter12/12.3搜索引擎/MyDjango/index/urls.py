from django.urls import path
from .views import MySearchView
urlpatterns = [
    # 搜索引擎
    path('', MySearchView.as_view(), name='haystack'),
]
