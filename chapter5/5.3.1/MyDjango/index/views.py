from django.views.generic.dates import MonthArchiveView
from .models import PersonInfo

class index(MonthArchiveView):
    allow_empty = True
    allow_future = True
    context_object_name = 'mylist'
    template_name = 'index.html'
    model = PersonInfo
    date_field = 'hireDate'
    queryset = PersonInfo.objects.all()
    year_format = '%Y'
    # month_format默认格式是支持英文日期，如Oct、Sep
    month_format = '%m'
    paginate_by = 50
