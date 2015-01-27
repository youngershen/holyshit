from django.contrib import admin
from .models import Post
from .models import Channel
from .models import PostReply
# Register your models here.


class ChannelAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


class PostReplyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(PostReply, PostReplyAdmin)