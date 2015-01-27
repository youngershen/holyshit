# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0004_auto_20150127_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='channel',
            field=models.ForeignKey(related_name='posts', to='chan.Channel'),
            preserve_default=True,
        ),
    ]
