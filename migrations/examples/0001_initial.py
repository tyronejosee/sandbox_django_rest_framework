# Generated by Django 5.0.6 on 2024-06-19 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Another',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_field', models.CharField(max_length=100)),
                ('text_field', models.TextField()),
                ('integer_field', models.IntegerField()),
                ('float_field', models.FloatField()),
                ('decimal_field', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_field', models.DateField()),
                ('time_field', models.TimeField()),
                ('date_time_field', models.DateTimeField()),
                ('boolean_field', models.BooleanField()),
                ('image_field', models.ImageField(upload_to='images/')),
                ('file_field', models.FileField(upload_to='files/')),
                ('url_field', models.URLField()),
                ('foreign_key_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examples.another')),
                ('many_to_many_field', models.ManyToManyField(to='examples.other')),
            ],
            options={
                'order_with_respect_to': 'foreign_key_field',
            },
        ),
    ]