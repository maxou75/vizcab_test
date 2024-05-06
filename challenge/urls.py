from django.urls import path

from . import views

urlpatterns = [
    path("total_surface_calculation", views.total_surface_calculation, name="total surface calculation"),
    path("building_usage", views.building_usage, name="building usage"),
]