# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import ckeditor.fields
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('created_on', models.DateTimeField(verbose_name='Время создания', default=django.utils.timezone.now)),
                ('published', models.BooleanField(verbose_name='Опубликован?', default=False)),
                ('published_on', models.DateTimeField(null=True, blank=True, verbose_name='Когда опубликовать')),
                ('annotation', ckeditor.fields.RichTextField(blank=True, max_length=1000, verbose_name='Аннотация')),
                ('content', ckeditor.fields.RichTextField(blank=True, max_length=5000, verbose_name='Текст')),
                ('image', models.ImageField(blank=True, upload_to=news.models.Event.upload_image_to, verbose_name='Изображение')),
            ],
            options={
                'verbose_name_plural': 'События',
                'verbose_name': 'Событие',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'Новости', 'verbose_name': 'Новость'},
        ),
        migrations.AddField(
            model_name='news',
            name='annotation',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1000, verbose_name='Аннотация'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, verbose_name='Текст'),
        ),
    ]
