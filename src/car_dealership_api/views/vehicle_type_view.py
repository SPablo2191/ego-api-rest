from rest_framework import viewsets
from ..serializers.vehicle_type_serializer import VehicleTypeSerializer
from ..models.vehicle_type import VehicleType


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
