# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_auto_20150120_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='slug',
            field=models.CharField(max_length=255, unique=True, null=True, verbose_name='board slug', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thread',
            name='slug',
            field=models.CharField(max_length=255, unique=True, null=True, verbose_name='thread slug', blank=True),
            preserve_default=True,
        ),
    ]
