# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_sitesettings_page_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='pagination_style',
            field=models.TextField(max_length=255, null=True, verbose_name='pagination stype', blank=True),
            preserve_default=True,
        ),
    ]
