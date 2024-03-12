from rest_framework import viewsets
from ..models.brand import Brand
from ..serializers.brand import BrandSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
