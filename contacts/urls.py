from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacts_page, name='contacts_page'),
    path('create/', views.contact_create, name='contact_create'),
    path('<int:pk>/edit/', views.contact_edit, name='contact_edit'),
]