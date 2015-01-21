# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen

from django.conf.urls import patterns, url

urlpatterns = patterns('bbs.views',
                       url(r'^$', 'bbs_index_view', name='bbs_index_view'),
                       url(r'thread/add/$', 'thread_add_view', name='bbs_thread_add_view'),
                       url(r'thread/add/action/$', 'thread_add_action', name='bbs_thread_add_action'),
                       url(r'board/(?P<slug>[-a-zA-Z0-9]+)/$', 'board_index_view', name='bbs_board_index_view'),
                       url(r'thread/(?P<slug>[-a-zA-Z0-9]+)/$', 'thread_index_view', name='bbs_thread_index_view')
                       )