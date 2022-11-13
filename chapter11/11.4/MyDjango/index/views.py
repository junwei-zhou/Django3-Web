from django.shortcuts import render
from .models import PersonInfo
from django.contrib import messages
from django.template import RequestContext
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView


# 视图函数使用消息框架
def index(request):
    # 筛选并保留比messages.WARNING级别高的消息提示
    # set_level必须在添加信息提示之前使用，否则无法筛选
    # messages.set_level(request, messages.WARNING)
    # 消息添加方法一
    messages.debug(request, 'debug类型')
    messages.info(request, 'info类型', 'MyInfo')
    messages.success(request, 'success类型')
    messages.warning(request, 'warning类型')
    messages.error(request, 'error类型')
    # 消息添加方法二
    messages.add_message(request, messages.INFO, 'info类型2')
    # 自定义消息类型
    # request代表参数request
    # 66代表参数level
    # 自定义类型代表参数message
    # MyDefine代表参数extra_tags
    messages.add_message(request, 66, '自定义类型', 'MyDefine')
    # 获取所以消息提示的最低级别
    current_level = messages.get_level(request)
    print(current_level)
    # 获取当前用户的消息提示对象
    mg = messages.get_messages(request)
    print(mg)
    return render(request, 'index.html', locals(), RequestContext(request))


# 视图类使用消息框架
def success(request):
    return render(request, 'index.html', locals(), RequestContext(request))


class iClass(SuccessMessageMixin, CreateView):
    model = PersonInfo
    fields = ['name', 'age']
    template_name = 'iClass.html'
    success_url = '/success'
    success_message = 'created successfully'
