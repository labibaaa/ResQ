from django.urls import path
from . import views

urlpatterns = [
    path('', views.guide_page, name='guide_page'),
    path('create/', views.guide_create, name='guide_create'),
    path('<int:pk>/edit/', views.guide_edit, name='guide_edit'),
]