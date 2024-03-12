from rest_framework import viewsets
from ..models.section import Section
from ..serializers.section_serializer import SectionSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
