from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import reverse

def mydate(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))

def index(request):
    print(reverse('index:turnTo'))
    return redirect(reverse('index:mydate', args=[2019,12,12]))
