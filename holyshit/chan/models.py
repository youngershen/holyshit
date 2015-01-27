from django.db import models
from django.utils.translation import ugettext_lazy as _
from unidecode import unidecode
from core.models import Entity
from sorl.thumbnail import ImageField
import time
# Create your models here.


class Channel(Entity):
    name = models.CharField(_("channel name"), max_length=255, unique=True, db_index=True)
    description = models.CharField(_("channel description"), max_length=255, null=True, blank=True)
    logo = ImageField(_('channel logo'), upload_to='channel/logo/%Y/%m/%d', null=True, blank=True)
    slug = models.CharField(_("channel slug"), max_length=255, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = '-'.join(unicode(unidecode(self.name)).split(' '))[:-1].lower()
        super(Channel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        print self
        return ''

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

    class Meta:
        verbose_name = _("channel")
        verbose_name_plural = _("channels")


class Post(Entity):
    title = models.CharField(_("post title"), max_length=255, db_index=True)
    content = models.TextField(_("post content"))
    ipaddress = models.IPAddressField(_("post author ip address"))
    author = models.CharField(_("post author"), max_length=255, null=True, blank=True)
    channel = models.ForeignKey('Channel', related_name='posts', on_delete=models.CASCADE)
    slug = models.CharField(_("post slug"), unique=True, max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = '-'.join(unicode(unidecode(self.title)).split(' ')).lower() + str(int(time.time()))
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return self

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.__str__()

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")


class PostReply(Entity):
    content = models.TextField(_("post reply content"))
    ipaddress = models.IPAddressField(_('post reply author ip address'))
    author = models.CharField(_("post reply author"), max_length=255, blank=True, null=True)

    reply_to = models.ForeignKey("Post", related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def __unicode__(self):
        return self.__str__()

    class Meta:
        verbose_name = _("post reply")
        verbose_name_plural = _("post replies")
