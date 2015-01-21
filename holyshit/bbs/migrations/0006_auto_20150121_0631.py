# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0005_auto_20150120_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'thread/%Y/%m/%d', null=True, verbose_name='thread image', blank=True),
            preserve_default=True,
        ),
    ]
