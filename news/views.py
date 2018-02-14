from django.views.generic import DetailView, ListView, View
from .models import *
from .settings import config
from django.http import JsonResponse
from django.utils import timezone


class NewsList (ListView):
    model = News
    template_name = config.NEWS_LIST_TEMPLATE


class NewsDetailView (DetailView):
    model = News
    template_name = config.NEWS_PAGE_TEMPLATE


class GetEvents(View):

    def get(self, request, *args, **kwargs):
        year = int(request.GET.get('year', timezone.now().year))
        month = request.GET.get('month', False)
        if month:
            month = int(month)+1
        else:
            month = timezone.now().month

        start = timezone.datetime(year=year, month=month, day=1, tzinfo=timezone.now().tzinfo)
        end = start + timezone.timedelta(days=35)
        events = Event.objects.filter(published=True, published_on__gte=start).filter(published_on__lte=end)
        data = {
            'error': 0,
            'events':
                [{
                    'id': e.pk,
                    'annotation': e.annotation,
                    'content': e.content,
                    'title': e.title,
                    'date': e.published_on.timestamp(),
                    'image': "<img src='%s' alt=''/>" % e.image.url if e.image else '',
                } for e in events]
        }

        return JsonResponse(data)
