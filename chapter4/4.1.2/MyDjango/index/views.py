from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import reverse
from django.shortcuts import render, redirect

def index(request):
    return redirect('index:shop' ,permanent=True)
    # 设置302的重定向
    # url = reverse('index:shop')
    # return HttpResponseRedirect(url)
    # 设置301的重定向
    # return HttpResponsePermanentRedirect(url)

def shop(request):
    return render(request, 'index.html')


