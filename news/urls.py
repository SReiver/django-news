from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', NewsList.as_view(), name="news-list"),
    url(r'^(?P<slag>\d+)/$', NewsDetailView.as_view(), name="news-detail"),
]