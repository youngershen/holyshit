# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0012_thread_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='music',
            field=models.FileField(upload_to=b'thread/music/%Y/%m/%d', null=True, verbose_name='thread music', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'thread/image/%Y/%m/%d', null=True, verbose_name='thread image', blank=True),
            preserve_default=True,
        ),
    ]
