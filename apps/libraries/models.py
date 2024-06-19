"""Models for Libraries App."""

from django.db import models
from polymorphic.models import PolymorphicModel


# Test for django-polymorphic
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


# Test for django-rest-framework-recursive
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
