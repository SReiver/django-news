from django.views.generic import DetailView, ListView
from .models import *
from .settings import config


class NewsList (ListView):
    model = News
    template_name = config.NEWS_LIST_TEMPLATE


class NewsDetailView (DetailView):
    model = News
    template_name = config.NEWS_PAGE_TEMPLATE
