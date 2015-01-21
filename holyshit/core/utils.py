# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen
from django.core.paginator import Paginator
from .models import SiteSettings
sitesetting = SiteSettings.objects.ordr_by('created_at')[0]


def pager(queryset):
    page_size = sitesetting.thread_page_size
    page_entity = Paginator(queryset, page_size)
    return page_entity