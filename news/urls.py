from django.conf.urls import url, include
from .views import *
from .admin import news_admin


urlpatterns = [
    url(r'^$', NewsList.as_view(), name="news-list"),
    url(r'^(?P<slag>\d+)/$', NewsDetailView.as_view(), name="news-detail"),
]