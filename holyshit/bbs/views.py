# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    :
# AUTHOR       : younger shen
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.views.generic import ListView, View, TemplateView
from .models import Board
from .models import Thread
from .forms import ThreadForm


class BoardIndexView(ListView):
    allow_empty = True
    template_name = 'bbs/board_index_view.html'
    model = Board
    paginate_by = 2
    paginate_orphans = 0
    context_object_name = 'objects'
    paginator_class = Paginator
    page_kwarg = 'page'
    ordering = '-created_at'

    def get(self, request, *args, **kwargs):
        try:
            board = Board.objects.get(slug=kwargs.get('slug'))
        except Board.DoesNotExist:
            raise Http404
        else:
            setattr(self, 'object_list', board.threads.order_by(self.ordering))
            allow_empty = self.get_allow_empty()
            if not allow_empty:
                if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                    is_empty = not self.object_list.exists()
                else:
                    is_empty = len(self.object_list) == 0
                if is_empty:
                    raise Http404
            context = self.get_context_data()
            return self.render_to_response(context)


class ThreadIndexView(ListView):
    template_name = 'bbs/thread_index_view.html'
    allow_empty = True
    model = Board
    paginate_by = 2
    paginate_orphans = 0
    context_object_name = 'objects'
    paginator_class = Paginator
    page_kwarg = 'page'
    ordering = '-created_at'

    def post(self, request, *args, **kwargs):
        addr = request.META.get('REMOTE_ADDR', '127.0.0.1')
        context = self.get_context_data(**kwargs)
        context.update(addr=addr)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        try:
            thread = Thread.objects.get(slug=kwargs.get('slug'))
        except Thread.DoesNotExist:
            raise Http404
        else:
            setattr(self, 'object_list', thread.children.order_by(self.ordering))
            allow_empty = self.get_allow_empty()
            if not allow_empty:
                if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                    is_empty = not self.object_list.exists()
                else:
                    is_empty = len(self.object_list) == 0
                if is_empty:
                    raise Http404
            context = self.get_context_data()
            return self.render_to_response(context)


class BbsIndexView(TemplateView):
    template_name = 'bbs/index.html'
    # http_method_names = ['GET', 'POST']

    def get_context_data(self, **kwargs):
        boards = Board.objects.order_by('-created_at')
        threads = Thread.objects.order_by('-created_at')
        form = ThreadForm()

        kwargs.update(dict(boards=boards, threads=threads, form=form))


class ThreadAddView(View):
    http_method_names = ['POST']

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(dict(state=True))
        else:
            return HttpResponse(dict(state=False))

