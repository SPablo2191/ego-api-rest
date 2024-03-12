from django.urls import path
from rest_framework import routers
from django.urls import path
from rest_framework import routers
from .views.data_sheet_view import DataSheetViewSet
from .views.vehicle_view import VehicleViewSet
from .views.vehicle_type_view import VehicleTypeViewSet
from .views.feature_view import FeatureViewSet
from .views.section_view import SectionViewSet

route = routers.SimpleRouter()
route.register("datasheet", DataSheetViewSet)
route.register("vehicles", VehicleViewSet)
route.register("categories", VehicleTypeViewSet)
route.register("features", FeatureViewSet)
route.register("sections", SectionViewSet)
