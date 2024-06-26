"""Admin for Products App."""

from django.contrib import admin

from .models import Category, Product, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price"]
    search_fields = ["name", "category__name"]
    list_filter = ["category"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["product", "rating", "created_at"]
    search_fields = ["product__name"]
    list_filter = ["rating", "created_at"]
