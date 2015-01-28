from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import bbs.urls
import chan.urls
import songtaste.urls
import reddit.urls
import account.urls

urlpatterns = patterns('',
                       url(r'^$', 'core.views.index_view', name='core_index_view'),
                       url(r'^about/$', 'core.views.about_view', name='core_about_view'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^bbs/', include(bbs.urls, namespace='bbs', app_name='bbs')),
                       # url(r'^reddit/', include(reddit.urls, namespace='reddit', app_name='reddit')),
                       # url(r'^account/', include(account.urls, namespace='account', app_name='account'))
                       # url(r'^chan/', include(chan.urls, namespace='chan', app_name=chan)),
                       # url(r'^songtaste/', include(songtaste.urls, namespace='songtaste', app_name='songtaste'))
                       )

handler404 = 'core.views.errors_handler_view'
handler403 = 'core.views.errors_handler_view'
handler400 = 'core.views.errors_handler_view'
handler500 = 'core.views.errors_handler_view'

if settings.DEBUG:
    # django debug toolbar
    import debug_toolbar
    urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)),)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
