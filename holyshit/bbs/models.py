import random
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
        self.slug = '-'.join(unicode(unidecode(self.name)).split(' ')).lower()
        super(Board, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

    class Meta:
        verbose_name = _('board')
        verbose_name_plural = _('boards')


class Thread(Entity):
    title = models.CharField(_('thread title'), max_length=255, db_index=True, null=True, blank=True)
    email = models.EmailField(_('thread author\'s email'), max_length=255, blank=True, null=True)
    author = models.CharField(_('thread author'), max_length=255, blank=True, null=True)
    ipaddress = models.IPAddressField(_('thread author\'s ip address'), max_length=255, null=True, blank=True)
    message = models.TextField(_('thread message'))
    image = ImageField(_('thread image'), upload_to='thread/%Y/%m/%d', null=True, blank=True)
    slug = models.CharField(_('thread slug'), max_length=255, unique=True, null=True, blank=True)
    click = models.BigIntegerField(_('thread click times'), default=0)
    link = models.CharField(_('website link'), max_length=255, null=True, blank=True)
    board = models.ForeignKey('Board', related_name='threads', on_delete=models.CASCADE, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.SET_NULL)

    @staticmethod
    def lattest_thread():
        return Thread.objects.order_by('-created_at')[:20]

    @staticmethod
    def hottest_thread():
        return Thread.objects.order_by('-click')[:20]

    def ordered_comments(self):
        return self.comments.order_by('-created_at')

    def add_click(self):
        setattr(self, 'click', self.click + 1)
        self.save()

    def up(self):
        setattr(self, 'click', self.click + 1)
        self.save()

    def down(self):
        setattr(self, 'click', self.click - 1)
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


class Comment(Entity):
    author = models.CharField(_('comment author'), max_length=255, null=True, blank=True)
    ipaddress = models.IPAddressField(_('comment author ip address'), max_length=255, null=True, blank=True)
    message = models.TextField(_('comment message'))

    thread = models.ForeignKey('Thread', related_name='comments', on_delete=models.CASCADE, blank=True, null=True)
    quote = models.OneToOneField('self', related_name='quotes', blank=True, null=True, on_delete=models.SET_NULL)

    def get_full_comment(self):
        ret_list = []
        this = self
        while True:
            if this.quote:
                ret_list.append(this.quote)
                this = this.quote
            else:
                return ret_list

    @staticmethod
    def get_random_template_style():
        return random.choice(['warning', 'info', 'success'])

    def __str__(self):
        return self.message

    def __unicode__(self):
        return self.__str__()

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

