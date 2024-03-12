from django.db import models
from django.contrib import admin
from .data_sheet import DataSheet
from .vehicle_type import VehicleType


class Vehicle(models.Model):
    model = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    data_sheet = models.ForeignKey(DataSheet, on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("model", "year", "price")
