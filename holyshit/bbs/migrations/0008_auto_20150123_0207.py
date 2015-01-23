# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0007_thread_click'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='content',
            new_name='message',
        ),
    ]
