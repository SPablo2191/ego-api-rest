from django.db import models
from django.contrib import admin
from .data_sheet import DataSheet


class Vehicle(models.Model):
    model = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    data_sheet = models.ForeignKey(DataSheet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("model", "year", "price")
