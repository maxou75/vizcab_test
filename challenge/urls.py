from django.urls import path

from . import views

urlpatterns = [
    path("total_surface", views.total_surface, name="total surface calculation"),
    path("building_usage", views.building_usage, name="building usage "),
    path("carbon_impact", views.carbon_impact, name="carbon impact calculation"),
]