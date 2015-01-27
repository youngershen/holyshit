# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen

from django.conf.urls import patterns, url

urlpatterns = patterns('reddit.views',
                       url(r'^$', 'index_view', name='reddit_index_view'),
                       )