from django.urls import path
from . import views

urlpatterns = [
    path('',                            views.dashboard,       name='dashboard'),
    path('vehicles/',                   views.vehicle_list,    name='vehicle_list'),
    path('vehicles/add/',               views.add_vehicle,     name='add_vehicle'),
    path('customers/',                  views.customer_list,   name='customer_list'),
    path('customers/add/',              views.add_customer,    name='add_customer'),
    path('rentals/',                    views.rental_history,  name='rental_history'),
    path('rentals/rent/',               views.rent_vehicle,    name='rent_vehicle'),
    path('rentals/return/<int:rental_id>/', views.return_vehicle, name='return_vehicle'),
]
