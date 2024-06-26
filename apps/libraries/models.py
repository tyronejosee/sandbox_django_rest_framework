"""Models for Libraries App."""

from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from mptt.models import MPTTModel, TreeForeignKey
from polymorphic.models import PolymorphicModel

# django-polymorphic
# https://django-polymorphic.readthedocs.io/en/stable/quickstart.html


class Animal(PolymorphicModel):
    name = models.CharField(max_length=100)

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def __str__(self):
        return self.name


class Dog(Animal):
    breed = models.CharField(max_length=100)

    def speak(self):
        return "Woof!"


class Cat(Animal):
    color = models.CharField(max_length=100)

    def speak(self):
        return "Meow!"


# django-rest-framework-recursive
# https://github.com/heywbj/django-rest-framework-recursive


class Comment(models.Model):
    text = models.TextField()
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.text


# Django MPTT
# https://django-mptt.readthedocs.io/en/latest/


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self) -> str:
        return self.name


# easy-thumbnails
# https://pypi.org/project/easy-thumbnails/

class Employee(models.Model):
    """Model definition for Employee."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    photo = ThumbnailerImageField(upload_to='employees/', blank=True)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    hire_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
