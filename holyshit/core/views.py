from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

# Create your views here.
from .models import SiteSettings

sitesettings = SiteSettings.objects.all()[0]


def index_view(request):
    return render(request, 'index.html', dict(sitesettings=sitesettings))


def about_view(request):
    return render(request, 'about.html', dict(sitesettings=sitesettings))


def page_not_found_view(request):
    return render(request, 'errors/404.html', dict(sitesettings=sitesettings))


def server_error_view(request):
    return render(request, 'errors/500.html', dict(sitesettings=sitesettings))


def permission_denied_view(request):
    return render(request, 'errors/403.html', dict(sitesettings=sitesettings))


def bad_request_view(request):
    return render(request, 'errors/400.html', dict(sitesettings=sitesettings))


def errors_handler_view(request):
    return redirect(reverse('bbs:board_hottest_view'))