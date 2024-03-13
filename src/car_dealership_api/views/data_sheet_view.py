from rest_framework import viewsets
from ..models.data_sheet import DataSheet
from ..serializers.data_sheet_serializer import DataSheetSerializer
from django_filters.rest_framework import DjangoFilterBackend


class DataSheetViewSet(viewsets.ModelViewSet):
    queryset = DataSheet.objects.all()
    serializer_class = DataSheetSerializer
    filter_backends = [DjangoFilterBackend]
    http_method_names = ["get", "post", "retrieve", "put", "patch"]
    filterset_fields = ["vehicle"]
