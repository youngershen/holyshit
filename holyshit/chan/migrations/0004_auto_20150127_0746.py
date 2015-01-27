# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0003_auto_20150127_0739'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostReply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='deleted at', blank=True)),
                ('content', models.TextField(verbose_name='post reply content')),
                ('ipaddress', models.IPAddressField(verbose_name='post reply author ip address')),
                ('author', models.TextField(max_length=255, null=True, verbose_name='post reply author', blank=True)),
                ('reply_to', models.ForeignKey(related_name='replies', to='chan.Post')),
            ],
            options={
                'verbose_name': 'post reply',
                'verbose_name_plural': 'post replies',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='post',
            name='reply_to',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=255, unique=True, null=True, verbose_name='post slug', blank=True),
            preserve_default=True,
        ),
    ]
