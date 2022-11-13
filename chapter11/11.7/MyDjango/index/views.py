from django.http import JsonResponse
from django.shortcuts import render
from .models import PersonInfo

def index(request):
    title = '首页'
    id = request.GET.get('id', 1)
    person = PersonInfo.objects.get(id=int(id))
    return render(request, 'index.html', locals())


def indexApi(request):
    id = request.GET.get('id', 1)
    person = PersonInfo.objects.get(id=int(id))
    rusult = {
        'name': person.name,
        'age': person.age
    }
    return JsonResponse(rusult)

