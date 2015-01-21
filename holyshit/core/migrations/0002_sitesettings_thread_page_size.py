# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='thread_page_size',
            field=models.IntegerField(default=20, verbose_name='thread page size'),
            preserve_default=True,
        ),
    ]
