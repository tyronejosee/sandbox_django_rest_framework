"""ViewSets for Libraries App."""

from rest_framework.viewsets import ModelViewSet

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
