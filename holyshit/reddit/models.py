from django.db import models

# Create your models here.
from unidecode import unidecode
from core.models import Entity
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Category(Entity):
    name = models.CharField(_("reddit category"), max_length=255, unique=True)
    description = models.TextField(_("reddit category description"), blank=True, null=True)
    slug = models.CharField(_("reddit category slug"), max_length=255, unique=True, blank=True, null=True)

    def get_absolute_url(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = '-'.join(unicode(unidecode(self.name)).split(' ')).lower()[:-1]

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __unicode(self):
        return self.__str__()

    class Meta:
        verbose_name = _("reddit category")
        verbose_name_plural = _("reddit categories")


class Link(Entity):
    name = models.CharField(_("link name"), max_length=255, blank=True, null=True)
    url = models.URLField(_("link url"), max_length=255, unique=True)
    description = models.TextField(_("link description"), blank=True, null=True)
    score = models.IntegerField(_("link score"), default=0)

    category = models.ForeignKey('Category', related_name='links', on_delete=models.CASCADE)
    def get_absolute_url(self):
        return self.name

    def up(self):
        setattr(self, 'score', self.score + 1)
        self.save()

    def down(self):
        setattr(self, 'score', self.score - 1)
        self.save()

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.url

        super(Link, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

    class Meta:
        verbose_name = _("reddit link")
        verbose_name_plural = _("reddit links")


class Comment(Entity):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments')
    content = models.CharField(_("content"), max_length=255)

    def __str__(self):
        return self.author

    def __unicode__(self):
        return self.__str__()

    class Meta:
        verbose_name = _("link comment")
        verbose_name_plural = _("link comments")

