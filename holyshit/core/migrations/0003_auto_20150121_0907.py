# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_sitesettings_thread_page_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitesettings',
            old_name='thread_page_size',
            new_name='page_size',
        ),
    ]
