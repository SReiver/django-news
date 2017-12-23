# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import news.models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=500)),
                ('created_on', models.DateTimeField(verbose_name='Время создания', default=django.utils.timezone.now)),
                ('published', models.BooleanField(verbose_name='Опубликован?', default=False)),
                ('published_on', models.DateTimeField(blank=True, verbose_name='Когда опубликовать', null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name='Текст новости', max_length=5000)),
                ('image', models.ImageField(blank=True, verbose_name='Изображение', upload_to=news.models.News.upload_image_to)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ('-published_on', 'pk'),
            },
        ),
    ]
