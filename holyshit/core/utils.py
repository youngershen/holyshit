# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from .models import SiteSettings
sitesetting = SiteSettings.objects.order_by('created_at')[0]


def paginator(queryset):
    page_size = sitesetting.page_size
    pager = Paginator(queryset, page_size)
    return pager


def bootstrap_pager(request, queryset):
    pager = paginator(queryset)
    try:
        page_number = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    try:
        current_page = pager.page(page_number)
    except EmptyPage:
        raise Http404
    else:
        objects = current_page.object_list
        count = pager.num_pages
        if current_page.has_other_pages():
            prev_page = page_number - 1
        else:
            prev_page = None

        if current_page.has_next():
            next_page = page_number + 1
        else:
            next_page = None

        # compute the page length
        page_length = 5
        page_list = list()
        left_page = page_length if page_number - page_length > 0 else page_number - 1
        right_page = page_length if page_number + page_length <= count else count - page_number

        for i in range(page_number - left_page, page_number + right_page + 1):
            page_list.append(i)

        return dict(page_list=page_list, objects=objects, count=count, prev_page=prev_page, next_page=next_page, page_number=page_number)