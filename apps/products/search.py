"""Search for Products App."""

from django_elasticsearch_dsl import Document, Index, fields

# from django_elasticsearch_dsl.registries import registry
from .models import Category, Product, Review

category_index = Index("category")
product_index = Index("product")
review_index = Index("review")


@category_index.doc_type
class CategoryDocument(Document):
    class Django:
        model = Category

    name = fields.TextField()
    description = fields.TextField()

    def prepare_name(self, instance):
        return instance.name

    def prepare_description(self, instance):
        return instance.description


@product_index.doc_type
class ProductDocument(Document):
    class Django:
        model = Product

    name = fields.TextField()
    description = fields.TextField()
    price = fields.FloatField()

    def prepare_name(self, instance):
        return instance.name

    def prepare_description(self, instance):
        return instance.description

    def prepare_price(self, instance):
        return float(instance.price)


@review_index.doc_type
class ReviewDocument(Document):
    class Django:
        model = Review

    rating = fields.IntegerField()
    comment = fields.TextField()
    created_at = fields.DateField()

    def prepare_rating(self, instance):
        return instance.rating

    def prepare_comment(self, instance):
        return instance.comment

    def prepare_created_at(self, instance):
        return instance.created_at
