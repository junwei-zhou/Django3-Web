
from django.urls import path, include
urlpatterns = [
    # 指向index的路由文件urls.py
    path('', include(('index.urls', 'index'), namespace='index')),
]
# 全局404页面配置
handler404 = 'index.views.pag_not_found'
# 全局500页面配置
handler500 = 'index.views.page_error'