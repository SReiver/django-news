from django import template
from django.template import loader, TemplateDoesNotExist
from news.models import News, Event
from django.utils import timezone
from django.core.urlresolvers import reverse, NoReverseMatch
import json

register = template.Library()


@register.simple_tag
def render_news(*args):
    tmp = loader.get_template('news/default_tag_list.html')
    if args:
        template_name = args[0]
        try:
            tmp = loader.get_template(template_name)
        except TemplateDoesNotExist:
            pass
    context = {'news': News.objects.filter(published=True, published_on__lte=timezone.now())}
    return tmp.render(context)


@register.simple_tag
def calendar(*args, **kwargs):

    tpl = loader.get_template('news/calendar.html')

    context = {
        'options': {
            'defaultView': 'month',
            'dateFormat': {'year': 'numeric', 'month': 'long', 'day': '2-digit'},
            'updateEvents': kwargs.get("updateEvents", 0)
        },
        'hasJQuery': kwargs.get('hasJQuery', 0),
        'calendarID': kwargs.get('calendarID', 'calendar'+str(timezone.now().microsecond))
    }
    if 'ajaxUrl' in kwargs:
        url = kwargs.get('ajaxUrl')
        if url == 1:
            url = reverse('news:events-ajax')
        elif url:
            try:
                url = reverse(kwargs.get('ajaxUrl'))
            except NoReverseMatch:
                url = kwargs.get('ajaxUrl')
        context['options']['ajaxUrl'] = url
    if 'dateFormat' in kwargs and kwargs.get("dateFormat"):
        context['options']['dateFormat'] = kwargs.get("dateFormat")
    if 'eventsList' in kwargs:
        events = kwargs.get('eventsList')
        if not isinstance(events, str):
            events = json.dumps(Event.serialise(events))
        context['options']['eventsList'] = events
    if 'fullEventTemplate' in kwargs:
        context['options']['fullEventTemplate'] = kwargs.get('fullEventTemplate')


    return tpl.render(context)
