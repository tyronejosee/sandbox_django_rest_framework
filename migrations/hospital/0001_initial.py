# Generated by Django 5.0.6 on 2024-06-25 23:27

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('specialty', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('birth_date', models.DateField()),
                ('city', models.CharField(max_length=30)),
                ('allergies', models.CharField(blank=True, max_length=80, null=True)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('province_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('admission_date', models.DateTimeField()),
                ('discharge_date', models.DateTimeField()),
                ('diagnosis', models.CharField(max_length=50)),
                ('attending_doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='province_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.province'),
        ),
    ]
