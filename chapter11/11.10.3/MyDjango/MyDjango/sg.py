from django.db.models.signals import post_save
from index.models import OrderInfo, ProductInfo

# 设置内置信号post_save的回调函数signal_post_save
def signal_orders(sender, **kwargs):
    print("pre_save is coming")
    # 输出sender的数据
    print(sender)
    # 输出kwargs的所有数据
    print(kwargs)
    # instance代表当前修改或新增的模型对象
    instance = kwargs.get('instance')
    # created判断当前操作是否在模型中新增数据，若新增数据则为True
    created = kwargs.get('created')
    # using代表当前使用的数据库
    # 如果连接了多个数据库，则显示当前修改或新增的数据表所在数据库的名称
    using = kwargs.get('using')
    # update_fields控制需要更新的字段，默认为None
    update_fields = kwargs.get('update_fields')

    # 当订单状态等于0的时候，说明订单已经取消，商品数量加1
    if instance.state == 0:
        p = ProductInfo.objects.get(id=instance.product_id)
        p.number += 1
        p.save()
    # 当订单状态等于1说明订单是新增，商品数量减1
    elif instance.state == 1:
        p = ProductInfo.objects.get(id=instance.product_id)
        p.number -= 1
        p.save()
# 将内置信号post_save与回调函数signal_post_save绑定
post_save.connect(signal_orders, sender=OrderInfo)



