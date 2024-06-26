"""Admin for Libraries App."""

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from polymorphic.admin import (
    PolymorphicChildModelAdmin,
    PolymorphicChildModelFilter,
    PolymorphicParentModelAdmin,
)

from .models import Animal, Cat, Category, Comment, Dog, Employee

# django-polymorphic
# https://django-polymorphic.readthedocs.io/en/stable/quickstart.html


@admin.register(Dog)
class DogAdmin(PolymorphicChildModelAdmin):
    base_model = Dog


@admin.register(Cat)
class CatAdmin(PolymorphicChildModelAdmin):
    base_model = Cat


@admin.register(Animal)
class AnimalAdmin(PolymorphicParentModelAdmin):
    base_model = Animal
    child_models = (Dog, Cat)
    list_filter = (PolymorphicChildModelFilter,)




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "parent",
    )
    list_filter = ("parent",)
    search_fields = ("text",)
    ordering = ("id",)


# Test for Django MPTT
# https://django-mptt.readthedocs.io/en/latest/

admin.site.register(Category, MPTTModelAdmin)

admin.site.register(Employee)
