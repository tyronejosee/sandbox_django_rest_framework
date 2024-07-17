"""Routers for Products App."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .views import (
    CategoryViewSet,
    ProductHistoryView,
    ProductSearchView,
    ProductViewSet,
    ReviewViewSet,
)

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")

categories_router = NestedSimpleRouter(router, r"categories", lookup="category")
categories_router.register(r"products", ProductViewSet, basename="category-products")

products_router = NestedSimpleRouter(categories_router, r"products", lookup="product")
products_router.register(r"reviews", ReviewViewSet, basename="product-reviews")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(categories_router.urls)),
    path("", include(products_router.urls)),
    path(
        "api/products/search/",
        ProductSearchView.as_view(),
    ),
    path(
        "api/products/<int:pk>/history/",
        ProductHistoryView.as_view(),
    ),
]
