import time
import asyncio
from asgiref.sync import sync_to_async
from .models import TaskInfo

# 异步任务
async def asyns():
    start = time.time()
    for num in range(1, 6):
        await asyncio.sleep(1)
        print('异步任务:', num)
    await sync_to_async(TaskInfo.objects.create,
                        thread_sensitive=True)(task='异步任务')
    print('异步任务Done, time used:', time.time()-start)

# 同步任务
def syns():
    start = time.time()
    for num in range(1, 6):
        time.sleep(1)
        print('同步任务:', num)
    TaskInfo.objects.create(task='同步任务')
    print('同步任务Done, time used:', time.time()-start)
