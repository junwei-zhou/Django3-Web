from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def myReplace(value, old='Jinja2', new='Django'):
    return str(value).replace(old, new)

# 将jinja2模版设置到项目环境
def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    env.filters['myReplace'] = myReplace
    return env