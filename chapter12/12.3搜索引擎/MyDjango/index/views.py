from django.core.paginator import *
from django.shortcuts import render
from django.conf import settings
from .models import *
from haystack.generic_views import SearchView
# 视图以通用视图实现
class MySearchView(SearchView):
    # 模版文件
    template_name = 'search.html'
    def get(self, request, *args, **kwargs):
        if not self.request.GET.get('q', ''):
            product = Product.objects.all().order_by('id')
            per = settings.HAYSTACK_SEARCH_RESULTS_PER_PAGE
            p = Paginator(product, per)
            try:
                num = int(self.request.GET.get('page', 1))
                page_obj = p.page(num)
            except PageNotAnInteger:
                # 如果参数page不是整型，则返回第1页数据
                page_obj = p.page(1)
            except EmptyPage:
                # 访问页数大于总页数，则返回最后1页的数据
                page_obj = p.page(p.num_pages)
            return render(request, self.template_name, locals())
        else:
            return super().get(*args, request, *args, **kwargs)