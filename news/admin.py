from django.contrib import admin
from .models import News, Event
from .settings import config


class NewsAdmin(admin.ModelAdmin):
    model = News
    search_fields = ('title', 'content')

admin.site.register(News, NewsAdmin)


class MyAdminSite(admin.AdminSite):
    pass


class NewsAdminSimple(admin.ModelAdmin):
    model = News
    search_fields = ('title', 'content')
    fields = config.NEWS_ADMIN_FIELDS

class EventAdminSimple(admin.ModelAdmin):
    model = Event
    search_fields = ('title', 'content')
    fields = config.EVENT_ADMIN_FIELDS


news_admin = MyAdminSite(name='news_admin')
news_admin.register(News, NewsAdminSimple)
news_admin.register(Event, EventAdminSimple)
