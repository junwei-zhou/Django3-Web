from django.shortcuts import render
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy

def index(request):
    if request.LANGUAGE_CODE == 'zh':
        language = gettext('Chinese')
        # language = gettext_lazy('Chinese')
    else:
        language = gettext('English')
        # language = gettext_lazy('English')
    print(language)
    return render(request, 'index.html', locals())
