from django.conf import settings


class config(object):
    NEWS_ADMIN_FIELDS = ('title', 'created_on', 'published', 'published_on', 'content', 'image')
    NEWS_LIST_TEMPLATE = 'news/default_list.html'
    NEWS_PAGE_TEMPLATE = 'news/default.html'

settings_config = getattr(settings, 'NEWS_ADMIN_FIELDS', False)
if settings_config:
    setattr(config, 'NEWS_ADMIN_FIELDS', settings_config)


NEWS_CKEDITOR_SETTINGS = {
    'language': 'ru-RU',
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['ShowBlocks'],
        ['Format', 'Styles'],
        ['Bold', 'Italic', 'Underline', '-','RemoveFormat'],
        [ 'Link', 'Unlink'],
        ['Source']
    ],
    'stylesSet': [
        {
            'name': 'Ссылка (открыть в этом окне)',
            'element': 'a',
            'attributes': {
                'class': 'href'
            }
        },
        {
            'name': 'Ссылка (открыть в новом окне)',
            'element': 'a',
            'attributes': {
                'class': 'href',
                'target': '_blank'
            }
        },
        {
            'name': 'Кнопка',
            'element': 'span',
            'attributes': {
                'class': 'button'
            }
        },
    ],
}

CKEDITOR_CONFIGS = {
    'news_editor': NEWS_CKEDITOR_SETTINGS
}