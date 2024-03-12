from rest_framework import viewsets
from ..serializers.vehicle_serializer import VehicleSerializer
from ..models.vehicle import Vehicle


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
