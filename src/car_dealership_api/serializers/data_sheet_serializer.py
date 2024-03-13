from rest_framework import serializers

from ..models.data_sheet import DataSheet
from ..models.feature import Feature

from .feature_serializer import FeatureSerializer

from .section_serializer import SectionSerializer


class DataSheetSerializer(serializers.ModelSerializer):

    data_sheet_feature = FeatureSerializer(many=True)
    data_sheet_section = SectionSerializer(many=True)

    class Meta:

        model = DataSheet

        fields = "__all__"

    def create(self, validated_data):
        data_sheet_feature = validated_data.pop("data_sheet_feature")
        data_sheet_section = validated_data.pop("data_sheet_section")
        data_sheet_instance = DataSheet.objects.create(**validated_data)
        for feature in data_sheet_feature:
            Feature.objects.create(user=data_sheet_instance, **feature)
        for section in data_sheet_section:
            Section.objects.create(user=data_sheet_instance, **section)
        return data_sheet_instance
