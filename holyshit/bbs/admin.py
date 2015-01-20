from django.contrib import admin
from .models import Board
from .models import Thread
# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    pass


class ThreadAdmin(admin.ModelAdmin):
    pass

admin.site.register(Thread, ThreadAdmin)
admin.site.register(Board, BoardAdmin)
