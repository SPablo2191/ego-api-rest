from django.db import models
from django.contrib import admin
from .feature import Feature
from .section import Section


class DataSheet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    features = models.ManyToManyField(Feature, through="feature_per_datasheet")
    sections = models.ManyToManyField(Section, through="section_per_datasheet")

    def __str__(self):
        return self.name


@admin.register(DataSheet)
class DataSheetAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
