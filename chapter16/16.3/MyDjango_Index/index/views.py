from django.http import JsonResponse
from .models import Product

def indexView(request):
    if request.method == 'GET':
        u = request.GET.get('username', '')
        if u:
            p = Product.objects.filter(user=u)
        else:
            p = Product.objects.all()
        result = []
        for i in p:
            value = {'username': i.user,
                     'name': i.name, 'type': i.type}
            result.append(value)
        return JsonResponse(result, safe=False)
