import time
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from unidecode import unidecode
from sorl.thumbnail import ImageField
# Create your models here.
from core.models import Entity


class Board(Entity):
    name = models.CharField(_('board name'), max_length=255, unique=True, db_index=True)
    description = models.TextField(_('board description'), null=True, blank=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.SET_NULL)
    slug = models.CharField(_('board slug'), max_length=255, unique=True, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('bbs:bbs_board_index_view', args=(self.slug,))

    def save(self, *args, **kwargs):
        self.slug = '-'.join(unicode(unidecode(self.name)).split(' ')).lower() + str(int(time.time()))
        super(Board, self).save(*args, **kwargs)

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
    ipaddress = models.IPAddressField(_('thread author\'s ip address'), max_length=255, null=True, blank=True)
    message = models.TextField(_('thread content'))
    image = ImageField(_('thread image'), upload_to='thread/%Y/%m/%d', null=True, blank=True)
    slug = models.CharField(_('thread slug'), max_length=255, unique=True, null=True, blank=True)
    click = models.BigIntegerField(_('thread click times'), default=0)

    board = models.ForeignKey('Board', related_name='threads', on_delete=models.CASCADE, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.SET_NULL)

    def add_click(self):
        # self.click = self.click + 1
        setattr(self, 'click', self.click + 1)
        self.save()

    def get_absolute_url(self):
        return reverse('bbs:bbs_thread', args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = '-'.join(unicode(unidecode(self.title)).split(' ')).lower() + str(int(time.time()))
        super(Thread, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.__str__()

    class Meta:
        verbose_name = _('thread')
        verbose_name_plural = _('threads')