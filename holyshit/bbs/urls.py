# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen

from django.conf.urls import patterns, url
from .views import BoardIndexView
from .views import ThreadIndexView
from .views import ThreadAddView
from .views import BbsIndexView

urlpatterns = patterns('bbs.views',
                       url(r'^$', BbsIndexView.as_view(), name='bbs_index'),
                       url(r'thread/add/$', ThreadAddView.as_view(), name='bbs_thread_add'),
                       url(r'board/(?P<slug>[-a-zA-Z0-9]+)/$', BoardIndexView.as_view(), name='bbs_board'),
                       url(r'thread/(?P<slug>[-a-zA-Z0-9]+)/$', ThreadIndexView.as_view(), name='bbs_thread')
                       )