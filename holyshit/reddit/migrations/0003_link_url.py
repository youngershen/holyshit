# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0002_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='url',
            field=models.URLField(default='', unique=True, max_length=255, verbose_name='link url'),
            preserve_default=False,
        ),
    ]
