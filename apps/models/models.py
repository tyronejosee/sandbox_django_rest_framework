"""Models for Models App."""

import uuid

from django.db import models


class RelatedModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Models(models.Model):

    # auto_field = models.AutoField()
    # big_auto_field = models.BigAutoField()
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=100)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField(upload_to="uploads/")
    file_field_and_field_file = models.FileField(upload_to="uploads/")
    file_path_field = models.FilePathField()
    float_field = models.FloatField()
    generated_field = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    generic_ip_address_field = models.GenericIPAddressField()
    image_field = models.ImageField(upload_to="images/")
    integer_field = models.IntegerField()
    json_field = models.JSONField()
    positive_big_integer_field = models.PositiveBigIntegerField()
    positive_integer_field = models.PositiveIntegerField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    slug_field = models.SlugField()
    # small_auto_field = models.SmallAutoField()
    small_integer_field = models.SmallIntegerField()
    text_field = models.TextField()
    time_field = models.TimeField()
    url_field = models.URLField()
    uuid_field = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    foreign_key = models.ForeignKey(
        RelatedModel, on_delete=models.CASCADE, related_name="models_foreign_keys"
    )
    many_to_many_field = models.ManyToManyField(
        RelatedModel, related_name="models_many_to_many"
    )
    one_to_one_field = models.OneToOneField(
        RelatedModel, on_delete=models.CASCADE, related_name="models_one_to_ones"
    )
