from django.views.generic import DetailView
from .models import PersonInfo
class index(DetailView):
    # 设置模版文件
    template_name = 'index.html'
    # 设置模型外的数据
    extra_context = {'title': '人员信息表'}
    # 设置模型的查询字段
    slug_field = 'age'
    # 设置路由的变量名，与属性slug_field实现模型的查询操作
    slug_url_kwarg = 'age'
    pk_url_kwarg = 'pk'
    # 设置查询模型PersonInfo
    model = PersonInfo
    # 属性queryset可以做简单的查询操作
    # queryset = PersonInfo.objects.all()
    # 如不设置，则模版上下文默认为personinfo
    # context_object_name = 'personinfo'
    # 是否将pk和slug作为查询条件
    # query_pk_and_slug = False

