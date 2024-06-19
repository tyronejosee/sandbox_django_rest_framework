"""Admin for Libraries App."""

from django.contrib import admin
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
    PolymorphicChildModelFilter,
)
from .models import Animal, Dog, Cat, Comment


# django-polymorphic
# https://django-polymorphic.readthedocs.io/en/stable/quickstart.html
class DogAdmin(PolymorphicChildModelAdmin):
    base_model = Dog


class CatAdmin(PolymorphicChildModelAdmin):
    base_model = Cat


@admin.register(Animal)
class AnimalAdmin(PolymorphicParentModelAdmin):
    base_model = Animal
    child_models = (Dog, Cat)
    list_filter = (PolymorphicChildModelFilter,)


admin.site.register(Dog, DogAdmin)
admin.site.register(Cat, CatAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "parent",
    )
    list_filter = ("parent",)
    search_fields = ("text",)
    ordering = ("id",)
