"""Views for Products App."""

from django_elasticsearch_dsl.search import Search
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ProductSearchView(APIView):
    def get(self, request):
        query = request.GET.get("q", "")
        search = Search(index="product")
        if query:
            search = search.query(
                "multi_match", query=query, fields=["name", "description"]
            )
        response = search.execute()
        results = [
            {
                "name": hit._source.name,
                "description": hit._source.description,
                "price": hit._source.price,
            }
            for hit in response
        ]
        return Response(results)
