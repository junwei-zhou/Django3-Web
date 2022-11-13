from django.http import HttpResponse
from MyDjango.sg import *

# 创建订单，触发post_save信号
def creatView(request):
    product_id = request.GET.get('product_id', '')
    buyer = request.GET.get('buyer', '')
    if product_id and buyer:
        o = OrderInfo(product_id=product_id, buyer=buyer)
        o.save()
        return HttpResponse('订单创建成功')
    return HttpResponse('参数无效')

# 如果使用update()修改数据，不会触发post_save信号
# 取消订单，触发post_save信号
def cancelView(request):
    id = request.GET.get('id', '')
    if id:
        o = OrderInfo.objects.get(id=int(id))
        # 判断订单状态
        if o.state == 1:
            o.state = 0
            o.save()
            return HttpResponse('订单取消成功')
        return HttpResponse('订单不符合取消条件')
    return HttpResponse('参数无效')
