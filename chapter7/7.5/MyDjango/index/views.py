from django.http import HttpResponse
from .models import createNewTab
import time

def indexView(request):
    today = time.localtime(time.time())
    model_name = f"sales{time.strftime('%Y-%m-%d',today)}"
    model_name = createNewTab(model_name)
    model_name.objects.create(
        product="Django",
        sales=666,
    )
    return HttpResponse('Done')