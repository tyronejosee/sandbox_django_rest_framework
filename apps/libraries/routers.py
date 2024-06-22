"""Routers for Libraries App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import CommentViewSet
from .views import category_tree_view

router = DefaultRouter()
router.register(r"comments", CommentViewSet, basename="comment")


urlpatterns = [
    path("api/", include(router.urls)),
    path("categories/", category_tree_view),
]
