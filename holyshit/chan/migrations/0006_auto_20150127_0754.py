# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0005_auto_20150127_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postreply',
            name='author',
            field=models.CharField(max_length=255, null=True, verbose_name='post reply author', blank=True),
            preserve_default=True,
        ),
    ]
