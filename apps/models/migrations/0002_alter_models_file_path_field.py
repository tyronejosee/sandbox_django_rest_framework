# Generated by Django 5.0.6 on 2024-07-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("models", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="models",
            name="file_path_field",
            field=models.FilePathField(),
        ),
    ]
