# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'Новости', 'verbose_name': 'Новость', 'ordering': ('-published_on', 'pk')},
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=djangocms_text_ckeditor.fields.HTMLField(verbose_name='Текст новости', max_length=5000, blank=True),
        ),
    ]
