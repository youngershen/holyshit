# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0006_auto_20150121_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='click',
            field=models.BigIntegerField(default=0, verbose_name='thread click times'),
            preserve_default=True,
        ),
    ]
