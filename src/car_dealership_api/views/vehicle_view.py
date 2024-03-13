from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from ..serializers.vehicle_serializer import VehicleSerializer
from ..models.vehicle import Vehicle


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ["get", "post", "retrieve", "put", "patch"]
    ordering_fields = ["model", "year", "price"]  # ordering
    filterset_fields = ["vehicle_type", "brand", "year"]
    search_fields = ["model"]  # search

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get("ordering", None)
        if ordering:
            return queryset.order_by(ordering)
        return queryset
