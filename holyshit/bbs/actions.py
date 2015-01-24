# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from bbs.forms import CommentForm, ThreadForm
from bbs.models import Thread


@require_POST
def thread_add_action(request):
    form = ThreadForm(request.POST, request.FILES)
    print request.FILES
    if form.is_valid():
        form.save()
        return JsonResponse(dict(state=True))
    else:
        return JsonResponse(dict(state=False, errors=form.errors.as_json()))


@require_POST
def thread_up_action(request):
    pk = request.POST.get('pk')
    try:
        thread = Thread.objects.get(pk=pk)
    except Thread.DoesNotExist:
        return JsonResponse(dict(state=False))
    else:
        thread.up()
        return JsonResponse(dict(state=True))


@require_POST
def thread_down_action(request):
    pk = request.POST.get('pk')
    try:
        thread = Thread.objects.get(pk=pk)
    except Thread.DoesNotExist:
        return JsonResponse(dict(state=False))
    else:
        thread.down()
        return JsonResponse(dict(state=True))


@require_POST
def comment_add_action(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse(dict(state=True))
    else:
        return JsonResponse(dict(state=False, messages=form.errors.as_json()))
