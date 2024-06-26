"""Admin for Reviews App."""

from django.contrib import admin

from .models import Comment, Post, Product


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "id",
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "id",
        "width",
        "height",
    ]
    readonly_fields = [
        "width",
        "height",
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "id",
    ]
