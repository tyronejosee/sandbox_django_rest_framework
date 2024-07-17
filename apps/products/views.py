"""Views for Products App."""

from django_elasticsearch_dsl.search import Search
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product, Review
from .serializers import (
    CategorySerializer,
    HistoricalProductSerializer,
    ProductSerializer,
    ReviewSerializer,
)


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


class ProductHistoryView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        history = product.history.all()
        serializer = HistoricalProductSerializer(history, many=True)
        return Response(serializer.data)

    # Example Data
    # [
    #     {
    #         "id": 7,
    #         "name": "Lorem 2",
    #         "description": "lorenaskdnaskndkasndkas",
    #         "price": "5.00",
    #         "history_date": "2024-07-17T17:58:48.540356Z",
    #         "history_user": 1,
    #         "history_type": "~",
    #     },
    #     {
    #         "id": 7,
    #         "name": "Lorem",
    #         "description": "lorenaskdnaskndkasndkas",
    #         "price": "5.00",
    #         "history_date": "2024-07-17T17:50:37.654793Z",
    #         "history_user": 1,
    #         "history_type": "+",
    #     },
    # ]
