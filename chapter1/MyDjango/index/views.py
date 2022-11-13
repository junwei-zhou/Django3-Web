from django.shortcuts import render
def index(request):
    value = 'This is test!'
    print(value)
    return render(request, 'index.html')