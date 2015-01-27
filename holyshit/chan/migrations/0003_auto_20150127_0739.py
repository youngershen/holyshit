# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0002_auto_20150127_0737'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=255, null=True, verbose_name='post slug', blank=True),
            preserve_default=True,
        ),
    ]
