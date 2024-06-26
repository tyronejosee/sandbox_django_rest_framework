"""Serializers for Reviews App."""

import uuid

from rest_framework import serializers

from .models import Comment, Post, Product


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def validate_object_id(self, value):
        try:
            uuid.UUID(str(value))
        except ValueError:
            raise serializers.ValidationError("Invalid UUID format.")
        return value

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
