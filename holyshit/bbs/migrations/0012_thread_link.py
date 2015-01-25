# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0011_auto_20150124_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='link',
            field=models.CharField(max_length=255, null=True, verbose_name='website link', blank=True),
            preserve_default=True,
        ),
    ]
