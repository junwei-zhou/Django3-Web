from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from .models import PersonInfo


def index(request, page):
    # 获取模型PersonInfo的全部数据
    person = PersonInfo.objects.all().order_by('-age')
    # 设置每一页的数据量为2
    p = Paginator(person, 2, 1)
    try:
        pages = p.get_page(page)
    except PageNotAnInteger:
        # 如果参数page的数据类型不是整型，就返回第一页数据
        pages = p.get_page(1)
    except EmptyPage:
        # 若用户访问的页数大于实际页数，则返回最后一页的数据
        pages = p.get_page(p.num_pages)
    return render(request, 'index.html', locals())
