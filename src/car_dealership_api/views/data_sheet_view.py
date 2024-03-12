from rest_framework import viewsets
from .models.data_sheet import DataSheet
from .serializers import DataSheetSerializer


class DataSheetViewSet(viewsets.ModelViewSet):
    queryset = DataSheet.objects.all()
    serializer_class = DataSheetSerializer
