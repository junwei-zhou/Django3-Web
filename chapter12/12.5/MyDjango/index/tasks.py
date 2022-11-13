from celery import shared_task
from .models import *
import time


@shared_task
def updateData(id, info):
    try:
        PersonInfo.objects.filter(id=id).update(**info)
        return 'Done'
    except:
        return 'Fail'


@shared_task
def timing():
    now = time.strftime("%H:%M:%S")
    with open("d:\\output.txt", "a") as f:
        f.write("The time is " + now)
        f.write("\n")
        f.close()
