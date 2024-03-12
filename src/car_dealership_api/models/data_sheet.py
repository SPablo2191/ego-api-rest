from django.db import models
from django.contrib import admin


class DataSheet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@admin.register(DataSheet)
class DataSheetAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
