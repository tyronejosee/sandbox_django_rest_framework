"""Views for Libraries App."""

from django.shortcuts import render

from .models import Category


def category_tree_view(request):
    categories = Category.objects.all()
    return render(request, "category_tree.html", {"categories": categories})
