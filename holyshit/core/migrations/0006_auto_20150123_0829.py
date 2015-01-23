# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_sitesettings_pagination_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='pagination_style',
            field=models.CharField(max_length=255, null=True, verbose_name='pagination stype', blank=True),
            preserve_default=True,
        ),
    ]
