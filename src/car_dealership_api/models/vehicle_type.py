from django.db import models
from django.contrib import admin


class VehicleType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    vehicles = models.ManyToManyField(Vehicle, through="vehicle_per_type")

    def __str__(self):
        return self.name


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
