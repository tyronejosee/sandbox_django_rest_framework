"""Choices for Reviews App."""

from django.db import models


class Category(models.TextChoices):

    PENDING = "pending", "Pending"
    ELECTRONICS = "electronics", "Electronics"
    BOOKS = "books", "Books"
    CLOTHING = "clothing", "Clothing"
    HOME = "home", "Home & Kitchen"
    BEAUTY = "beauty", "Beauty & Health"
