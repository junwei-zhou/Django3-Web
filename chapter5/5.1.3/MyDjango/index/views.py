from django.views.generic import ListView
from .models import PersonInfo
class index(ListView):
    # 设置模版文件
    template_name = 'index.html'
    # 设置模型外的数据
    extra_context = {'title': '人员信息表'}
    # 查询模型PersonInfo
    queryset = PersonInfo.objects.all()
    # 每页的展示一条数据
    paginate_by = 1
    # 如不设置，则模版上下文默认为personinfo_list
    # context_object_name = 'personinfo'

