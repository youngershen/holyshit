# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    :
# AUTHOR       : younger shen

from django.http import Http404
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_GET
from .models import Board
from .models import Thread
from .forms import ThreadForm
from core.models import SiteSettings
from core.utils import bootstrap_pager


sitesettings = SiteSettings.objects.order_by('-created_at')[0]


@require_GET
def bbs_index_view(request):
    return redirect(reverse('bbs:board_hottest_view'))

@require_GET
def board_index_view(request, slug):
    try:
        board = Board.objects.get(slug=slug)
    except Board.DoesNotExist:
        raise Http404
    else:
        boards = Board.objects.order_by('-created_at')
        threads = board.threads.order_by('-created_at')
        board_name = board.name
        form = ThreadForm()
        page_info = bootstrap_pager(request, threads)

        ipaddress = request.META.get('REMOTE_ADDR', '127.0.0.1')
        base_url = reverse('bbs:bbs_board_index_view', args=(slug, ))
        ret = dict(form=form, boards=boards, board_name=board_name, threads=page_info['objects'], base_url=base_url, ipaddress=ipaddress, board=board, pagination_style=sitesettings.pagination_style)
        ret.update(page_info)
        return render(request, 'bbs/index.html', ret)


@require_GET
def thread_index_view(request, slug):
    print slug
    try:
        thread = Thread.objects.get(slug=slug)
    except Thread.DoesNotExist:
        raise Http404
    else:
        thread.add_click()
        threads = thread.children.order_by('-created_at')
        return render(request, 'bbs/thread_index_view.html', dict(thread=thread, threads=threads))


@require_GET
def board_hottest_view(request):
    threads = Thread.objects.order_by('-click')
    boards = Board.objects.order_by('-created_at')
    board_name = 'hottest'
    page_info = bootstrap_pager(request, threads)
    form = ThreadForm()
    base_url = reverse('bbs:board_hottest_view')
    ret = dict(boards=boards, threads=page_info['objects'], board_name=board_name, base_url=base_url, form=form, pagination_style=sitesettings.pagination_style)
    ret.update(page_info)
    return render(request, 'bbs/index.html', ret)


