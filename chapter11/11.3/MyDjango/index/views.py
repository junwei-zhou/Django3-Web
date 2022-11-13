from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

# 添加CSRF防护
# @csrf_protect
# 取消CSRF防护
@csrf_exempt
def index(request):
    return render(request, 'index.html')

