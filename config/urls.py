"""
URL configuration for config project.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# from django.views.generic.base import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    # Apps urls
    path("", include("apps.reviews.routers")),
]


# Debug config
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# AdminSite props.
admin.site.site_header = "Sandbox DRF"
admin.site.site_title = "Sandbox DRF"
admin.site.index_title = "Admin"
