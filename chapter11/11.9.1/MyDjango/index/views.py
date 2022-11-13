from django.shortcuts import render
from .models import PersonInfo
from concurrent.futures import ThreadPoolExecutor
import datetime, time

def indexView(request):
    startTime = datetime.datetime.now()
    print(startTime)
    title = '单线程'
    results = []
    for i in range(2):
        person = PersonInfo.objects.filter(id=int(i+1)).first()
        time.sleep(3)
        results.append(person)
    endTime = datetime.datetime.now()
    print(endTime)
    print('单线程查询所花费时间', endTime-startTime)
    return render(request, 'index.html', locals())



# 定义多线程任务
def get_info(id):
    person = PersonInfo.objects.filter(id=int(id)).first()
    time.sleep(3)
    return person

def threadIndexView(request):
    # 计算运行时间
    startTime = datetime.datetime.now()
    print(startTime)
    title = '多线程'
    Thread = ThreadPoolExecutor(max_workers=2)
    results = []
    fs = []
    # 执行多线程
    for i in range(2):
        t = Thread.submit(get_info, i + 1)
        fs.append(t)
    # 获取多线程的执行结果
    for t in fs:
        results.append(t.result())
    # 计算运行时间
    endTime = datetime.datetime.now()
    print(endTime)
    print('多线程查询所花费时间', endTime-startTime)
    return render(request, 'index.html', locals())