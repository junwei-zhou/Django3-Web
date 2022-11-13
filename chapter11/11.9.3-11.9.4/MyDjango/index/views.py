import asyncio
from django.http import HttpResponse
from .tasks import syns, asyns
from asgiref.sync import async_to_sync, sync_to_async

# 同步视图 -调用同步任务
def synView(request):
    # # 同步视图 - 调用异步任务
    # # 异步任务转为同步任务
    # w = async_to_sync(asyns)
    # # 调用函数
    # w()
    syns()
    return HttpResponse("Hello, This is syns!")

# 异步视图 - 调用异步任务
async def asynView(request):
    # # 异步视图 - 调用同步任务
    # # 同步任务转为异步任务
    # a = sync_to_async(syns)
    # # 调用函数
    # loop = asyncio.get_event_loop()
    # loop.create_task(a())
    loop = asyncio.get_event_loop()
    loop.create_task(asyns())
    return HttpResponse("Hello, This is asyns!")




