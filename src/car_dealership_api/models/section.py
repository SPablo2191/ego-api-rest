from django.db import models
from django.contrib import admin
from .data_sheet import DataSheet


class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField(max_length=100)
    data_sheet = models.ForeignKey(
        DataSheet,
        on_delete=models.CASCADE,
        related_name="data_sheet_section",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
