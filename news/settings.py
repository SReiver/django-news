from django.conf import settings


class config(object):
    NEWS_ADMIN_FIELDS = ('title', 'created_on', 'published', 'published_on', 'content', 'image')
    NEWS_LIST_TEMPLATE = 'news/default_list.html'
    NEWS_PAGE_TEMPLATE = 'news/default_page.html'

settings_config = getattr(settings, 'NEWS_ADMIN_FIELDS', False)
if settings_config:
    setattr(config, 'NEWS_ADMIN_FIELDS', settings_config)
