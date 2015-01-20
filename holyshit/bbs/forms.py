# -*- coding:utf-8 -*-
# PROJECT_NAME : holyshit
# FILE_NAME    : 
# AUTHOR       : younger shen
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from .models import Thread


class ThreadForm(ModelForm):

    def clean(self):
        print self.fields
        raise ValidationError(_('test validator'), code='test')

    class Meta:
        model = Thread
        fields = ['title', 'email', 'author', 'content', 'image']
        labels = {
            'title': _('title'),
            'email': _('email'),
            'author': _('author'),
            'content': _('content'),
            'image': _('image')
        }
        help_texts = {
            'title': _('thread title'),
            'email': _('author email'),
            'author': _('author name'),
            'content': _('thread content'),
            'image': _('thread image')
        }
        error_messages = {
            'title': {
                'required': _('title is required'),
                'test': _('title validator test')
            }
        }