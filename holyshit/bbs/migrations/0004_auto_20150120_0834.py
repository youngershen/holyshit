# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_auto_20150120_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='board',
            field=models.ForeignKey(related_name='threads', blank=True, to='bbs.Board', null=True),
            preserve_default=True,
        ),
    ]
