from django.urls import path
from . import views
urlpatterns = [
    # 添加带有字符类型、整型和slug的路由
    path('<year>/<int:month>/<slug:day>', views.mydate, name='mydate'),
    # 定义首页的路由
    path('', views.index, name='index')
]
