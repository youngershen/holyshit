# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen

from django.conf.urls import patterns, url

urlpatterns = patterns('bbs.views',
                       url(r'^$', 'bbs_index', name='bbs_index'),
                       url(r'board/(?P<slug>[-a-zA-Z0-9]+)/$', 'board_index', name='bbs_board_index'),
                       url(r'thread/(?P<slug>[-a-zA-Z0-9]+)/$', 'thread_index', name='bbs_thread_index')
                       )