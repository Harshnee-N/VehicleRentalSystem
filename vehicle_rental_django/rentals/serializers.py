from rest_framework import serializers
from .models import Vehicle, Customer, Rental


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Vehicle
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Customer
        fields = '__all__'


class RentalSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.customer_name', read_only=True)
    vehicle_name  = serializers.CharField(source='vehicle.vehicle_name',  read_only=True)

    class Meta:
        model  = Rental
        fields = [
            'rental_id', 'customer', 'customer_name',
            'vehicle', 'vehicle_name',
            'days_rented', 'total_amount'
        ]


class RentVehicleSerializer(serializers.Serializer):
    """Used for POST /api/rentals/rent/"""
    customer_id = serializers.IntegerField()
    vehicle_id  = serializers.IntegerField()
    days_rented = serializers.IntegerField(min_value=1)
