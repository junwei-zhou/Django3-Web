from django.shortcuts import render
from django.views.generic.base import RedirectView

def index(request):
    return render(request, 'index.html')

class turnTo(RedirectView):
    permanent = False
    url = None
    pattern_name = 'index:index'
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        print('This is get_redirect_url')
        return super().get_redirect_url(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        print(request.META.get('HTTP_USER_AGENT'))
        return super().get(request, *args, **kwargs)