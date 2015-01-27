# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0003_link_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='category',
            field=models.ForeignKey(related_name='links', default='', to='reddit.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='link',
            name='description',
            field=models.TextField(null=True, verbose_name='link description', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='link',
            name='score',
            field=models.IntegerField(default=0, verbose_name='link score'),
            preserve_default=True,
        ),
    ]
