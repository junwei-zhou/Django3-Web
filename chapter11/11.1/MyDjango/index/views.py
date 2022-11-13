from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login')
def index(request):
    # 获取GET请求参数
    id = request.GET.get('id', '')
    if id:
        # 获取存储在Session的idList
        # 如果Session不存在idList，则返回一个空列表
        idList = request.session.get('idList', [])
        # 判断当前请求参数是否已存储在Session
        if not id in idList:
            # 将商品的主键id存储在idList
            idList.append(id)
        # 更新Session的idList
        request.session['idList'] = idList
        return redirect('/')
    # 查询所有商品信息
    products = Product.objects.all()
    return render(request, 'index.html', locals())


# 订单确认
def orderView(request):
    # 获取存储在Session的idList
    # 如果Session不存在idList，则返回一个空列表
    idList = request.session.get('idList', [])
    # 获取GET请求参数，如果没有请求参数，返回空值
    del_id = request.GET.get('id', '')
    # 判断是否为空，若非空，删除Session里的商品信息
    if del_id in idList:
        # 删除Session里某个商品的主键
        idList.remove(del_id)
        # 将删除后的数据覆盖原来的Session
        request.session['idList'] = idList
    # 根据idList查询商品的所有信息
    products = Product.objects.filter(id__in=idList)
    return render(request, 'order.html', locals())
