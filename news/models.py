from django.db import models
from django.utils import timezone
import os
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField


class News(models.Model):

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'
        ordering = ('-published_on', 'pk')

    def upload_image_to(instance, filename):
        return os.path.join('news', str(instance.pk or 'new'), filename)

    title = models.CharField(max_length=500, verbose_name="Заголовок")
    created_on = models.DateTimeField(default=timezone.now, verbose_name='Время создания')
    published = models.BooleanField(blank=True, default=False, verbose_name="Опубликован?")
    published_on = models.DateTimeField(blank=True, null=True, verbose_name="Когда опубликовать")
    content = RichTextField(blank=True, max_length=5000, verbose_name="Текст новости", config_name='news_editor')
    image = models.ImageField(blank=True, verbose_name="Изображение", upload_to=upload_image_to)

    def __str__(self):
        ttl = "%s (%s)" % (self.title, self.created_on.strftime("%d.%m.%y %H:%M"))
        if not self.published:
            ttl = "<span style='color:#cacaca;'>%s</span>" % ttl
        return mark_safe(ttl)

    def save(self, *args, **kwargs):
        if not self.published_on and self.published:
            self.published_on = timezone.now()
        if not self.title:
            from django.utils import formats
            self.title = formats.date_format(self.published_on, 'd E Y') if self.published_on \
                else formats.date_format(self.created_on, 'Создан d E Y')
        super(News, self).save(*args, **kwargs)
