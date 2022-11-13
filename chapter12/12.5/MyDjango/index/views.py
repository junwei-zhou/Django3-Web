from django.http import HttpResponse
from .tasks import updateData


def index(request):
    # 传递参数并执行异步任务
    id = request.GET.get('id', 1)
    info = dict(name='May', age=19, hireDate='2019-10-10')
    updateData.delay(id, info)
    return HttpResponse("Hello Celery")
