"""Admin for Reviews App."""

from django.contrib import admin

from .models import Post, Product, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "user",
    ]
