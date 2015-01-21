from django.contrib import admin
from .models import SiteSettings
from .models import Advertisement
# Register your models here.


class SiteSettingsAdmin(admin.ModelAdmin):
    pass


class AdvertisementAdmin(admin.ModelAdmin):
    pass

admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)

