from django.urls import path
from . import views
urlpatterns = [
    # 添加带有字符类型、整型和slug的URL
    path('<year>/<int:month>/<slug:day>', views.myvariable),
    # 添加路由地址信息外的变量month
    path('', views.index, {'month': '2019/10/10'})
]
