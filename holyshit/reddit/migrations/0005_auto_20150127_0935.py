# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reddit', '0004_auto_20150127_0935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='deleted at', blank=True)),
                ('content', models.CharField(max_length=255, verbose_name='content')),
                ('author', models.ForeignKey(related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'link comment',
                'verbose_name_plural': 'link comments',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': 'reddit link', 'verbose_name_plural': 'reddit links'},
        ),
    ]
