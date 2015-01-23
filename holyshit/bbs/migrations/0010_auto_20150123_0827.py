# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='message',
            field=models.TextField(verbose_name='thread message'),
            preserve_default=True,
        ),
    ]
