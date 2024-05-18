import uuid
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType

from .mod


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
        content_type = validated_data.get("content_type")
        # object_id = validated_data.get("object_id")

        if not ContentType.objects.filter(id=content_type.id).exists():
            raise serializers.ValidationError("Invalid content type.")

        return super().create(validated_data)
