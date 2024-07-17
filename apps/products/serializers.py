from rest_framework import serializers

from .models import Category, Product, Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            "id",
            "rating",
            "comment",
            "created_at",
        ]


class ProductSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "reviews",
        ]


class CategorySerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "description",
            "products",
        ]


class HistoricalProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product.history.model
        fields = [
            "id",
            "name",
            "description",
            "price",
            "history_date",
            "history_user",
            "history_type",
        ]
