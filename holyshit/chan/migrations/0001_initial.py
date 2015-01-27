# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='deleted at', blank=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='channel name', db_index=True)),
                ('description', models.CharField(max_length=255, null=True, verbose_name='channel description', blank=True)),
                ('logo', sorl.thumbnail.fields.ImageField(upload_to=b'channel/logo/%Y/%m/%d', null=True, verbose_name='channel logo', blank=True)),
                ('slug', models.CharField(max_length=255, unique=True, null=True, verbose_name='channel slug', blank=True)),
            ],
            options={
                'verbose_name': 'channel',
                'verbose_name_plural': 'channels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='deleted at', blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='post title', db_index=True)),
                ('content', models.TextField(verbose_name='post content')),
                ('ipaddress', models.IPAddressField(verbose_name='post author ip address')),
                ('author', models.CharField(max_length=255, null=True, verbose_name='post author', blank=True)),
                ('slug', models.CharField(max_length=255, unique=True, null=True, verbose_name='post slug', blank=True)),
                ('channel', models.ForeignKey(related_name='posts', to='chan.Channel')),
                ('reply_to', models.ForeignKey(related_name='properties', blank=True, to='chan.Post', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
