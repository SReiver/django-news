# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20171020_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published_on',
            field=models.DateTimeField(verbose_name='Когда опубликовать', null=True, blank=True),
        ),
    ]
