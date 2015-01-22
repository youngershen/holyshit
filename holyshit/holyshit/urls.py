from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import bbs.urls

urlpatterns = patterns('',
                       url(r'^$', 'core.views.index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'bbs/', include(bbs.urls, namespace='bbs', app_name='bbs')),
                       )


if settings.DEBUG:
    # django debug toolbar
    import debug_toolbar
    # urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)),)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
