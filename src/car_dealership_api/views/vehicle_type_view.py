from rest_framework import viewsets
from .serializers import VehicleTypeSerializer
from .models import VehicleType


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
