from django.conf import settings


class config(object):
    NEWS_ADMIN_FIELDS = ('title', 'created_on', 'published', 'published_on', 'annotation', 'content', 'image')
    NEWS_LIST_TEMPLATE = 'news/default_list.html'
    NEWS_PAGE_TEMPLATE = 'news/default_page.html'
    EVENT_ADMIN_FIELDS = NEWS_ADMIN_FIELDS

settings_config = getattr(settings, 'NEWS_SETTINGS', {})
for k in settings_config:
    if hasattr(config, k):
        setattr(config, k, settings_config[k])
