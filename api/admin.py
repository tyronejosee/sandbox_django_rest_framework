"""Pending."""

from django.contrib import admin
from api.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin View for Post"""
