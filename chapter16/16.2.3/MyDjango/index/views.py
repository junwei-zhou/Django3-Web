from django.http import JsonResponse
from .models import Product


def index(request):
    if request.method == 'GET':
        u = request.GET.get('username', '')
        if u:
            infos = Product.objects.filter(user__username=u)
        else:
            infos = Product.objects.all()
        result = []
        for i in infos:
            value = {'username': i.user.username, 'name': i.name, 'type': i.type}
            result.append(value)
        return JsonResponse(result, safe=False)