# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='deleted at', blank=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='board name', db_index=True)),
                ('description', models.TextField(null=True, verbose_name='board description', blank=True)),
                ('parent', models.ForeignKey(related_name='children', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='bbs.Board', null=True)),
            ],
            options={
                'verbose_name': 'board',
                'verbose_name_plural': 'boards',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='deleted at', blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='thread title', db_index=True)),
                ('email', models.EmailField(max_length=255, null=True, verbose_name="thread author's email", blank=True)),
                ('author', models.CharField(max_length=255, null=True, verbose_name='thread author', blank=True)),
                ('ipaddress', models.IPAddressField(verbose_name="thread author's ip address")),
                ('content', models.TextField(verbose_name='thread content')),
                ('image', models.ImageField(upload_to=b'', null=True, verbose_name='thread image', blank=True)),
                ('board', models.ForeignKey(related_name='threads', to='bbs.Board')),
                ('parent', models.ForeignKey(related_name='children', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='bbs.Thread', null=True)),
            ],
            options={
                'verbose_name': 'thread',
                'verbose_name_plural': 'threads',
            },
            bases=(models.Model,),
        ),
    ]
