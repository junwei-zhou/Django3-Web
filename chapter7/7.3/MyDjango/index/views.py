from django.shortcuts import render
from .models import *
from django.db import transaction
from django.db.models import F

@transaction.atomic
def index(request):
    # 开启事务保护
    sid = transaction.savepoint()
    try:
        id = request.GET.get('id', '')
        if id:
            v = Vocation.objects.filter(id=id)
            v.update(payment=F('payment') + 1)
            print('Done')
            # 提交事务
            # 如不设置，当程序执行完成后，会自动提交事务
            # transaction.savepoint_commit(sid)
        else:
            # 全表的payment字段自减1
            Vocation.objects.update(payment=F('payment') - 1)
            # 事务回滚，将全表payment字段自减1的操作撤回
            transaction.savepoint_rollback(sid)
    except Exception as e:
        # 事务回滚
        transaction.savepoint_rollback(sid)
    return render(request, 'index.html', locals())
