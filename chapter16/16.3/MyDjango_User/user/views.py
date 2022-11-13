from django.http import JsonResponse
from django.contrib.auth.models import User

def userView(request):
    if request.method == 'GET':
        u = request.GET.get('username', '')
        user = User.objects.filter(username=u).first()
        result = {'id': user.id}
        return JsonResponse(result, safe=False)