# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0004_auto_20150120_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='ipaddress',
            field=models.IPAddressField(null=True, verbose_name="thread author's ip address", blank=True),
            preserve_default=True,
        ),
    ]
