# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='image',
            field=models.ImageField(upload_to=b'thread/%Y/%m/%d', null=True, verbose_name='thread image', blank=True),
            preserve_default=True,
        ),
    ]
