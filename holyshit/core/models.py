from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.


class Entity(models.Model):

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    deleted_at = models.DateTimeField(_('deleted at'), null=True, blank=True)

    class Meta:
        abstract = True


class SiteSettings(Entity):
    site_title = models.CharField(_('site title'), max_length=255)
    analytics_code = models.TextField(_('site analytics code'), blank=True, null=True)
    Announcement = models.TextField(_('site announcement'), blank=True, null=True)

    def __str__(self):
        return self.site_title

    def __unicode__(self):
        return self.__str__()


class Advertisement(Entity):
    name = models.CharField(_('ad name'), max_length=255)
    code = models.TextField(_('add code'), blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()