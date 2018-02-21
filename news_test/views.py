from django.views.generic.base import TemplateView
from news.models import Event


class DemoView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(DemoView, self).get_context_data(**kwargs)
        context.update({
            'events': Event.objects.filter(published=True)
        })
        return context
