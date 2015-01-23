# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    :
# AUTHOR       : younger shen

from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
from django.conf import settings
from .models import Board
from .models import Thread
from .forms import ThreadForm
from core.models import SiteSettings
from core.utils import bootstrap_pager


sitesettings = SiteSettings.objects.order_by('-created_at')[0]


@require_GET
def bbs_index_view(request):
    boards = Board.objects.order_by('-created_at')
    if boards.count() > 0:
        threads = boards[0].threads.order_by('-created_at')
    else:
        threads = []

    sitesttings = SiteSettings.objects.order_by('created_at')

    if sitesttings.count() > 0:
        sitesetting = sitesttings[0]
    else:
        sitesetting = dict(site_title=settings.SITE_TITLE)

    return render(request, 'bbs/index.html', dict(boards=boards, threads=threads, sitesetting=sitesetting))


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
        ipaddress = request.META.get('REMOTE_ADDR', '127.0.0.1')
        base_url = reverse('bbs:bbs_board_index_view', args=(slug, ))
        return render(request, 'bbs/index.html', dict(form=form, boards=boards, board_name=board_name, threads=threads, base_url=base_url, ipaddress=ipaddress, board=board))


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


@require_POST
def thread_add_action(request):
    form = ThreadForm(request.POST, request.FILES)
    print request.FILES
    if form.is_valid():
        form.save()
        return JsonResponse(dict(state=True))
    else:
        return JsonResponse(dict(state=False, errors=form.errors.as_json()))


@require_GET
def board_hottest_view(request):
    threads = Thread.objects.order_by('-click')
    boards = Board.objects.order_by('-created_at')
    board_name = 'hottest'
    page_info = bootstrap_pager(request, threads)
    form = ThreadForm()
    ret = dict(boards=boards, threads=page_info['objects'], board_name=board_name)
    base_url = reverse('bbs:board_hottest_view')
    ret.update(page_info)
    ret.update(dict(base_url=base_url, form=form))
    return render(request, 'bbs/index.html', ret)