from rest_framework import viewsets
from ..serializers.feature_serializer import FeatureSerializer
from ..models.feature import Feature


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
