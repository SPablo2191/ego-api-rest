from rest_framework import viewsets
from ..serializers.vehicle_serializer import VehicleSerializer
from ..models.vehicle import Vehicle


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    ordering_fields = ["model", "year", "price"]

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get("ordering", None)
        if ordering:
            return queryset.order_by(ordering)
        return queryset
