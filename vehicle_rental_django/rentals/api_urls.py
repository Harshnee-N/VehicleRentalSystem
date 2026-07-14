from django.urls import path
from . import api_views

urlpatterns = [
    # Vehicles
    path('vehicles/',               api_views.api_vehicles,       name='api_vehicles'),
    path('vehicles/<int:pk>/',      api_views.api_vehicle_detail, name='api_vehicle_detail'),

    # Customers
    path('customers/',              api_views.api_customers,       name='api_customers'),
    path('customers/<int:pk>/',     api_views.api_customer_detail, name='api_customer_detail'),

    # Rentals
    path('rentals/',                api_views.api_rental_history,  name='api_rental_history'),
    path('rentals/rent/',           api_views.api_rent_vehicle,    name='api_rent_vehicle'),
    path('rentals/<int:rental_id>/return/', api_views.api_return_vehicle, name='api_return_vehicle'),
]
