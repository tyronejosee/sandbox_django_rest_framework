"""Admin for Hospital App."""

from django.contrib import admin

from .models import Patient, Doctor, Admission, Province


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """Admin for Patient model."""

    list_display = (
        "first_name",
        "last_name",
        "gender",
        "birth_date",
        "city",
        "province_id",
        "height",
        "weight",
    )
    search_fields = ("first_name", "last_name", "city")
    list_filter = ("gender", "city")


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Admin for Doctor model."""


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    """Admin for Admission model."""


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    """Admin for Province model."""
