from rest_framework import serializers
from .models.data_sheet import DataSheet


class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = "__all__"
