# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150121_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='page_length',
            field=models.IntegerField(default=5, verbose_name='thread paginator length'),
            preserve_default=True,
        ),
    ]
