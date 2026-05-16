from django.urls import path
from . import views

urlpatterns = [
    path('', views.aid_page, name='aid_page'),
    path('donate/cash/', views.donate_cash, name='donate_cash'),
    path('donate/goods/', views.donate_goods, name='donate_goods'),
    path('donations/', views.donation_list, name='donation_list'),
    path('donations/cash/<int:pk>/verify/', views.verify_cash_donation, name='verify_cash'),
    path('donations/goods/<int:pk>/received/', views.mark_goods_received, name='goods_received'),
    path('stats/update/', views.update_lives_saved, name='update_lives_saved'),
]