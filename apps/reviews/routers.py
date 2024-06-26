"""Routers for Reviews App."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import CommentViewSet, PostViewSet, ProductViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"products", ProductViewSet)
router.register(r"comments", CommentViewSet)


urlpatterns = [
    path("api/v1/", include(router.urls)),
]
