from django.urls import path
from . import views

urlpatterns = [
    path('', views.evacuation_page, name='evacuation_page'),
    path('zones.json', views.safe_zones_json, name='safe_zones_json'),
    path('zones/create/', views.zone_create, name='zone_create'),
    path('zones/<int:pk>/edit/', views.zone_edit, name='zone_edit'),
    path('zones/<int:pk>/occupancy/', views.update_occupancy, name='update_occupancy'),
]