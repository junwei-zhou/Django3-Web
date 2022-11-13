from django.views.generic.dates import WeekArchiveView
from .models import PersonInfo

class index(WeekArchiveView):
    allow_empty = True
    allow_future = True
    context_object_name = 'mylist'
    template_name = 'index.html'
    model = PersonInfo
    date_field = 'hireDate'
    queryset = PersonInfo.objects.all()
    year_format = '%Y'
    week_format = '%W'
    paginate_by = 50
