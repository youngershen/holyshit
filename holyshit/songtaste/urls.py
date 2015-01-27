# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen

from django.conf.urls import patterns, url

urlpatterns = patterns('songtaste.views',
                       url(r'^$', 'index_view', name='songtaste_index_view'),
                       )


urlpatterns += patterns('songtaste.actions',

                        )