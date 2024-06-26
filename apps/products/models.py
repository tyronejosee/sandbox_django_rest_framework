"""Models for Products App."""

from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ["pk"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)


class Product(models.Model):

    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["pk"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return str(self.name)


class Review(models.Model):

    product = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE
    )
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review of {self.product.name} by {self.id}"
