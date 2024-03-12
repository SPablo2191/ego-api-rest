from django.db import models
from django.contrib import admin
from .vehicle_type import VehicleType
from .brand import Brand


class Vehicle(models.Model):
    model = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.model} {self.model} ({self.year})"


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("model", "year", "price")
