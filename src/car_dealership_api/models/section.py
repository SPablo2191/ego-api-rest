from django.db import models
from django.contrib import admin


class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
