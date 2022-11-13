from django.http import JsonResponse
import requests

def apiView(request):
    if request.method == 'GET':
        u = request.GET.get('username', '')
        url = 'http://127.0.0.1:%s/?username=%s'
        result = []
        if u:
            user = requests.get(url %('8081', u))
            id = user.json().get('id')
            products = requests.get(url %('8082', id))
            temp = products.json()
        else:
            products = requests.get(url % ('8082', ''))
            temp = products.json()
        for i in temp:
            value = {'username': i['username'],
                     'name': i['name'], 'type': i['type']}
            result.append(value)
        return JsonResponse(result, safe=False)
