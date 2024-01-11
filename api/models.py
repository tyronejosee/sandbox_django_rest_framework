"""Pending."""

from django.db import models


class Post(models.Model):
    """Model definition for Post."""

    title = models.CharField(max_length=50, null=False, blank=True)
    body = models.TextField(max_length=5000, null=False, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return str(self.title)
