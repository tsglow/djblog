from django.contrib import admin
from .models import Author, Post, Tag
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("first_name", "last_name")
    list_display = ("first_name", "last_name")

class TagAdmin(admin.ModelAdmin):
    list_filter = ("caption",)
    list_display = ("caption",)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}
    list_filter = ("title", "author")
    list_display = ("title", "author", "date")

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
