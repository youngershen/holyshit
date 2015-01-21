# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    :
# AUTHOR       : younger shen
from coffin.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
from .models import Board
from .models import Thread
from .forms import ThreadForm


@require_GET
def bbs_index(request):
    return HttpResponse('index')


@require_GET
def board_index(request, slug):
    try:
        board = Board.objects.get(slug=slug)
    except Board.DoesNotExist:
        raise Http404
    else:
        threads = board.threads.order_by('-created_at')
        return render('bbs/board_index_view.html', dict(threads=threads))


@require_GET
def thread_index(request, slug):
    try:
        thread = Thread.objects.get(slug=slug)
    except Thread.DoesNotExist:
        raise Http404
    else:
        threads = thread.children.order_by('-created_at')
        return render('bbs/thread_index_view.html', dict(thread=thread, threads=threads))

