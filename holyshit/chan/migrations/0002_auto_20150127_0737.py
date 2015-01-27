# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='channel',
            field=models.ForeignKey(related_name='posts', blank=True, to='chan.Channel', null=True),
            preserve_default=True,
        ),
    ]
