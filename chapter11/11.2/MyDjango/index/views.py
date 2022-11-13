from django.shortcuts import render
# 导入cache_page
from django.views.decorators.cache import cache_page
# 参数cache与配置属性CACHE_MIDDLEWARE_ALIAS相同
# 参数key_prefix与配置属性CACHE_MIDDLEWARE_KEY_PREFIX相同
# 参数timeout与配置属性CACHE_MIDDLEWARE_SECONDS相同
# CACHE_MIDDLEWARE_SECONDS的优先级高于参数timeout
# @cache_page(timeout=10, cache='MyDjango', key_prefix='MyView')
def index(request):
    return render(request, 'index.html')
