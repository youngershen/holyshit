# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='deleted at', blank=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='reddit category')),
                ('description', models.TextField(null=True, verbose_name='reddit category description', blank=True)),
                ('slug', models.CharField(max_length=255, unique=True, null=True, verbose_name='reddit category slug', blank=True)),
            ],
            options={
                'verbose_name': 'reddit category',
                'verbose_name_plural': 'reddit categories',
            },
            bases=(models.Model,),
        ),
    ]
