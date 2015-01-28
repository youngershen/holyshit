# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen
import logging
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from django.conf import settings
from .models import Thread
from .models import Comment

logger = logging.getLogger("holyshit")


class ThreadForm(ModelForm):

    def clean(self):
        image_file = self.cleaned_data.get('image', None)
        if image_file:
            ext = str(image_file).lower().split('.')[-1]
            if ext not in settings.IMAGE_ALLOW_FILE_TYPE:
                raise ValidationError(_('not allowed image file type'), code='image_type_error')

        music_file = self.cleaned_data.get('music', None)
        if music_file:
            ext = str(music_file).lower().split('.')[-1]
            if ext not in settings.MUSIC_ALLOW_FILE_TYPE:
                raise ValidationError(_('not allowed music file type'), code='music_type_error')

    class Meta:
        model = Thread
        fields = ['title', 'email', 'author', 'message', 'image', 'ipaddress', 'board', 'link', 'music']
        labels = {
            'title': _('title'),
            'email': _('email'),
            'author': _('author'),
            'message': _('message'),
            'image': _('image'),
            'link': _('link'),
            'music': _('music')
        }
        help_texts = {
            'title': _('thread title'),
            'email': _('author email'),
            'author': _('author name'),
            'message': _('thread message'),
            'image': _('thread image'),
            'link': _('website link'),
            'music': _('thread music')
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
            },
            'image:': {
                'image_type_error': _('image file type not allowed')
            },
            'music': {
                'music_type_error': _('music file type not allowed')
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