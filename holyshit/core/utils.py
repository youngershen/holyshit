# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from .models import SiteSettings
sitesetting = SiteSettings.objects.ordr_by('created_at')[0]


def paginator(queryset):
    page_size = sitesetting.page_size
    pager = Paginator(queryset, page_size)
    return pager


def bootstrap_pager(request, queryset):
    pager = paginator(queryset)
    page_number = request.GET.get('page', 1)

    try:
        current_page = pager.page(page_number)
    except EmptyPage:
        raise Http404
    else:
        objects = pager.object_list
        count = pager.count
        if current_page.has_other_pages():
            prev_page = page_number - 1
        else:
            prev_page = -1

        if current_page.has_next():
            next_page = page_number + 1
        else:
            next_page = -1

        # compute the page length
        page_length = 5
        page_list = list()
        left_page = page_length if page_number - page_length > 0 else abs(page_number - page_length)
        right_page = page_length if page_number + page_length < count + 1 else count - page_number
        for i in range(left_page, right_page):
            page_list.append(i)

        return dict(page_list=page_list, object=objects, count=count, prev_page=prev_page, next_page=next_page, page_number=page_number)