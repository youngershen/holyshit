# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from .models import Thread
from .models import Comment


class ThreadForm(ModelForm):

    def clean(self):
        # print self.fields
        # raise ValidationError(_('test validator'), code='test')
        pass

    class Meta:
        model = Thread
        fields = ['title', 'email', 'author', 'message', 'image', 'ipaddress', 'board', 'link']
        labels = {
            'title': _('title'),
            'email': _('email'),
            'author': _('author'),
            'message': _('message'),
            'image': _('image'),
            'link': _('link')
        }
        help_texts = {
            'title': _('thread title'),
            'email': _('author email'),
            'author': _('author name'),
            'message': _('thread message'),
            'image': _('thread image'),
            'link': _('website link')
        }
        error_messages = {
            'email': {
                'invalid': _('email format is invalid')
            },
            'message': {
                'required': _('message is required')
            },
            'link': {
                'url': _(''),
                'magnet': _(''),
                'ed2k': _('')
            }
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'message', 'thread']
        labels = {
            'author': _('author'),
            'message': _('message'),
            'thread': _('thread')
        }
        help_texts = {
            'author': _('comment author'),
            'message': _('comment message'),
            'thread': _('comment thread')
        }
        error_messages={
            'message': {
                'required': _('message is required')
            }
        }