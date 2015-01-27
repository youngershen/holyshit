# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen

from django.conf.urls import patterns, url

urlpatterns = patterns('account.views',
                       url(r'^$', 'index_view', name='account_index_view'),
                       url(r'profile/$', 'profile_view', name='account_profile_view'),
                       url(r'login/$', 'login_view', name='account_login_view'),
                       url(r'regist/$', 'regist_view', name='account_regist_view')
                       )

urlpatterns += patterns('account.actions',
                        url(r'login/action/$', 'login_action', name="account_login_action")
                        )