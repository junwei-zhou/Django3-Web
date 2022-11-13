
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('', include(('user.urls', 'user'), namespace='user')),
    # 导入Django Simple Captcha的路由，生成图片地址
    path('captcha/', include('captcha.urls'))
]
