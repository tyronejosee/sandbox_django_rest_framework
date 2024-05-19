"""ViewSets for Reviews App."""

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post, Product, Comment
from .serializers import PostSerializer, ProductSerializer, CommentSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=False, methods=["get"])
    def post_comments(self, request):
        post_comments = Comment.objects.filter(content_type__model="post")
        serializer = self.get_serializer(post_comments, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def product_comments(self, request):
        product_comments = Comment.objects.filter(content_type__model="product")
        serializer = self.get_serializer(product_comments, many=True)
        return Response(serializer.data)
