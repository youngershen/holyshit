from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from core.models import Entity


class Board(Entity):
    name = models.CharField(_('board name'), max_length=255, unique=True, db_index=True)
    description = models.TextField(_('board description'), null=True, blank=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

    class Meta:
        verbose_name = _('board')
        verbose_name_plural = _('boards')


class Thread(Entity):
    title = models.CharField(_('thread title'), max_length=255, db_index=True)
    email = models.EmailField(_('thread author\'s email'), max_length=255, blank=True, null=True)
    author = models.CharField(_('thread author'), max_length=255, blank=True, null=True)
    ipaddress = models.IPAddressField(_('thread author\'s ip address'), max_length=255)
    content = models.TextField(_('thread content'))
    image = models.ImageField(_('thread image'), upload_to='thread/%Y/%m/%d', null=True, blank=True)

    board = models.ForeignKey('Board', related_name='threads', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.__str__()

    class Meta:
        verbose_name = _('thread')
        verbose_name_plural = _('threads')