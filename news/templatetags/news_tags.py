from django import template
from django.template import loader, TemplateDoesNotExist
from news.models import News
from django.utils import timezone
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