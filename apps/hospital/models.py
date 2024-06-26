"""Models for Hospital App."""

import uuid

from django.db import models


class Patient(models.Model):
    """Model definition for Patient."""

    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    city = models.CharField(max_length=30)
    province_id = models.ForeignKey("Province", on_delete=models.CASCADE)
    allergies = models.CharField(max_length=80, blank=True, null=True)
    height = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Doctor(models.Model):
    """Model definition for Doctor."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    specialty = models.CharField(max_length=25)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"


class Admission(models.Model):
    """Model definition for Admission."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admission_date = models.DateTimeField()
    discharge_date = models.DateTimeField()
    diagnosis = models.CharField(max_length=50)
    attending_doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient_id} by {self.attending_doctor_id}"


class Province(models.Model):
    """Model definition for Province."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    province_name = models.CharField(max_length=30)

    def __str__(self):
        return self.province_name
