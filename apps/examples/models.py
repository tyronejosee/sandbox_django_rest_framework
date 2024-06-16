"""Models for Examples App."""

from django.db import models


class Field(models.Model):
    """Model definition for Field."""

    # Text fields
    char_field = models.CharField(max_length=100)
    text_field = models.TextField()

    # Numeric fields
    integer_field = models.IntegerField()
    float_field = models.FloatField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)

    # Date and time fields
    date_field = models.DateField()
    time_field = models.TimeField()
    date_time_field = models.DateTimeField()

    # Boolean field
    boolean_field = models.BooleanField()

    # Fields for relationships
    foreign_key_field = models.ForeignKey("Another", on_delete=models.CASCADE)
    many_to_many_field = models.ManyToManyField("Other")

    # Other fields
    image_field = models.ImageField(upload_to="images/")
    file_field = models.FileField(upload_to="files/")
    url_field = models.URLField()

    class Meta:
        order_with_respect_to = "foreign_key_field"


class Another(models.Model):
    """Model definition for Another."""

    name = models.CharField(max_length=100)


class Other(models.Model):
    """Model definition for Other."""

    name = models.CharField(max_length=100)
