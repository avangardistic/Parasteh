from django.contrib import admin

from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
    )
    search_fields = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
