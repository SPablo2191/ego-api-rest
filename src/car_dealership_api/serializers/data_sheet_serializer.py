from rest_framework import serializers
from ..models.data_sheet import DataSheet
from .feature_serializer import FeatureSerializer
from .section_serializer import SectionSerializer


class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = "__all__"
