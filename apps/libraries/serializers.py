"""Serializers for Libraries App."""

from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Comment


# Test for django-rest-framework-recursive
# https://github.com/heywbj/django-rest-framework-recursive


class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, required=False)

    class Meta:
        model = Comment
        fields = [
            "id",
            "text",
            "parent",
            "children",
        ]
