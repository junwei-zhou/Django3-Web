from django.views.generic.base import TemplateView

class index(TemplateView):
    template_name = 'index.html'
    template_engine = None
    content_type = None
    extra_context = {'title': 'This is GET'}

    # 重新定义模版上下文的获取方式
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['value'] = 'I am MyDjango'
        return context

    # 定义HTTP的POST请求处理
    def post(self, request, *args, **kwargs):
        self.extra_context = {'title': 'This is POST'}
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)