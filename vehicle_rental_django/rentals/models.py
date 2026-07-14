from django.db import models


class Vehicle(models.Model):
    """Maps to your Vehicle class + vehicles table"""

    VEHICLE_TYPES = [
        ('Car', 'Car'),
        ('Bike', 'Bike'),
        ('Truck', 'Truck'),
    ]

    vehicle_id   = models.AutoField(primary_key=True)
    vehicle_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_TYPES)
    rent_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    available    = models.BooleanField(default=True)

    class Meta:
        db_table = 'vehicles'   # uses your existing MySQL table

    def __str__(self):
        return f"{self.vehicle_name} ({self.vehicle_type})"


class Customer(models.Model):
    """Maps to your Customer class + customers table"""

    customer_id   = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    phone         = models.CharField(max_length=15)

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return f"{self.customer_name} - {self.phone}"


class Rental(models.Model):
    """Maps to your Rental class + rentals table"""

    rental_id    = models.AutoField(primary_key=True)
    customer     = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='customer_id')
    vehicle      = models.ForeignKey(Vehicle,  on_delete=models.CASCADE, db_column='vehicle_id')
    days_rented  = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'rentals'

    @staticmethod
    def calculate_bill(rent_per_day, days):
        """Reused from your original Rental class"""
        return rent_per_day * days

    def __str__(self):
        return f"Rental #{self.rental_id} - {self.customer.customer_name}"
