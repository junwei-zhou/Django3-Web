from django.shortcuts import render
def indexView(request):
    value = 'This is test!'
    print(value)
    return render(request, 'index.html')