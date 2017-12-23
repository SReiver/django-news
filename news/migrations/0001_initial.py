# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import news.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=500)),
                ('created_on', models.DateTimeField(verbose_name='Время создания', default=django.utils.timezone.now)),
                ('published', models.BooleanField(verbose_name='Опубликован?', default=False)),
                ('published_on', models.DateTimeField(null=True, blank=True, verbose_name='Когда опубликован')),
                ('content', models.TextField(blank=True, verbose_name='Текст новости', max_length=5000)),
                ('image', models.ImageField(blank=True, verbose_name='Изображение', upload_to=news.models.News.upload_presentation_to)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
