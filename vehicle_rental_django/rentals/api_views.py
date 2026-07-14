from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Vehicle, Customer, Rental
from .serializers import (
    VehicleSerializer, CustomerSerializer,
    RentalSerializer, RentVehicleSerializer
)


# ── VEHICLES API ──────────────────────────────────────────

@api_view(['GET', 'POST'])
def api_vehicles(request):
    """
    GET  /api/vehicles/       → list all available vehicles
    POST /api/vehicles/       → add a new vehicle
    """
    if request.method == 'GET':
        vehicles = Vehicle.objects.filter(available=True)
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def api_vehicle_detail(request, pk):
    """
    GET    /api/vehicles/<id>/  → get single vehicle
    DELETE /api/vehicles/<id>/  → delete vehicle
    """
    vehicle = get_object_or_404(Vehicle, pk=pk)

    if request.method == 'GET':
        return Response(VehicleSerializer(vehicle).data)

    elif request.method == 'DELETE':
        vehicle.delete()
        return Response({'message': 'Vehicle deleted'}, status=status.HTTP_204_NO_CONTENT)


# ── CUSTOMERS API ─────────────────────────────────────────

@api_view(['GET', 'POST'])
def api_customers(request):
    """
    GET  /api/customers/  → list all customers
    POST /api/customers/  → add a new customer
    """
    if request.method == 'GET':
        customers = Customer.objects.all()
        return Response(CustomerSerializer(customers, many=True).data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_customer_detail(request, pk):
    """GET /api/customers/<id>/"""
    customer = get_object_or_404(Customer, pk=pk)
    return Response(CustomerSerializer(customer).data)


# ── RENTALS API ───────────────────────────────────────────

@api_view(['GET'])
def api_rental_history(request):
    """GET /api/rentals/ → full rental history with customer & vehicle names"""
    rentals = Rental.objects.select_related('customer', 'vehicle').all()
    return Response(RentalSerializer(rentals, many=True).data)


@api_view(['POST'])
def api_rent_vehicle(request):
    """
    POST /api/rentals/rent/
    Body: { "customer_id": 1, "vehicle_id": 2, "days_rented": 3 }
    """
    serializer = RentVehicleSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data       = serializer.validated_data
    vehicle    = get_object_or_404(Vehicle, pk=data['vehicle_id'], available=True)
    customer   = get_object_or_404(Customer, pk=data['customer_id'])
    days       = data['days_rented']
    total      = Rental.calculate_bill(float(vehicle.rent_per_day), days)

    rental = Rental.objects.create(
        customer=customer,
        vehicle=vehicle,
        days_rented=days,
        total_amount=total
    )

    vehicle.available = False
    vehicle.save()

    return Response({
        'message':      'Vehicle rented successfully!',
        'rental_id':    rental.rental_id,
        'customer':     customer.customer_name,
        'vehicle':      vehicle.vehicle_name,
        'days_rented':  days,
        'total_amount': f'₹{total}'
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def api_return_vehicle(request, rental_id):
    """POST /api/rentals/<id>/return/ → mark vehicle as returned"""
    rental = get_object_or_404(Rental, pk=rental_id)
    rental.vehicle.available = True
    rental.vehicle.save()
    return Response({'message': f'Vehicle "{rental.vehicle.vehicle_name}" returned successfully!'})
