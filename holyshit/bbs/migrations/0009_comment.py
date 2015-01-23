# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0008_auto_20150123_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='deleted at', blank=True)),
                ('author', models.CharField(max_length=255, null=True, verbose_name='comment author', blank=True)),
                ('ipaddress', models.IPAddressField(null=True, verbose_name='comment author ip address', blank=True)),
                ('message', models.TextField(verbose_name='comment message')),
                ('quote', models.OneToOneField(related_name='quotes', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='bbs.Comment')),
                ('thread', models.ForeignKey(related_name='comments', blank=True, to='bbs.Thread', null=True)),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
            bases=(models.Model,),
        ),
    ]
