from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Link
from .models import Comment


class CategoryAdmin(admin.ModelAdmin):
    pass


class LinkAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Comment, CommentAdmin)

