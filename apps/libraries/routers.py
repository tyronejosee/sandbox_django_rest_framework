"""Routers for Libraries App."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import category_tree_view
from .viewsets import CommentViewSet

router = DefaultRouter()
router.register(r"comments", CommentViewSet, basename="comment")


urlpatterns = [
    path("api/", include(router.urls)),
    path("api/categories/", category_tree_view),
]
