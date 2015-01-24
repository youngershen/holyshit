# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0010_auto_20150123_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='title',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='thread title', blank=True),
            preserve_default=True,
        ),
    ]
