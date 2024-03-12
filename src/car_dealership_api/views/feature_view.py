from rest_framework import viewsets
from .serializers import FeatureSerializer
from .models import Feature


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
