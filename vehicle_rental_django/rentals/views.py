from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Vehicle, Customer, Rental


# ── VEHICLES ──────────────────────────────────────────────

def vehicle_list(request):
    """View all available vehicles"""
    vehicles = Vehicle.objects.filter(available=True)
    return render(request, 'rentals/vehicle_list.html', {'vehicles': vehicles})


def add_vehicle(request):
    """Add a new vehicle"""
    if request.method == 'POST':
        name         = request.POST.get('vehicle_name')
        vehicle_type = request.POST.get('vehicle_type')
        rent         = request.POST.get('rent_per_day')
        Vehicle.objects.create(
            vehicle_name=name,
            vehicle_type=vehicle_type,
            rent_per_day=rent
        )
        messages.success(request, f'Vehicle "{name}" added successfully!')
        return redirect('vehicle_list')
    return render(request, 'rentals/add_vehicle.html')


# ── CUSTOMERS ─────────────────────────────────────────────

def customer_list(request):
    """View all customers"""
    customers = Customer.objects.all()
    return render(request, 'rentals/customer_list.html', {'customers': customers})


def add_customer(request):
    """Add a new customer"""
    if request.method == 'POST':
        name  = request.POST.get('customer_name')
        phone = request.POST.get('phone')
        Customer.objects.create(customer_name=name, phone=phone)
        messages.success(request, f'Customer "{name}" added successfully!')
        return redirect('customer_list')
    return render(request, 'rentals/add_customer.html')


# ── RENTALS ───────────────────────────────────────────────

def rent_vehicle(request):
    """Rent a vehicle to a customer"""
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        vehicle_id  = request.POST.get('vehicle_id')
        days        = int(request.POST.get('days_rented'))

        vehicle  = get_object_or_404(Vehicle, pk=vehicle_id, available=True)
        customer = get_object_or_404(Customer, pk=customer_id)

        total = Rental.calculate_bill(float(vehicle.rent_per_day), days)

        Rental.objects.create(
            customer=customer,
            vehicle=vehicle,
            days_rented=days,
            total_amount=total
        )

        vehicle.available = False
        vehicle.save()

        messages.success(request, f'Vehicle rented! Total Bill: ₹{total}')
        return redirect('rental_history')

    vehicles  = Vehicle.objects.filter(available=True)
    customers = Customer.objects.all()
    return render(request, 'rentals/rent_vehicle.html', {
        'vehicles': vehicles,
        'customers': customers
    })


def rental_history(request):
    """View full rental history with JOIN"""
    rentals = Rental.objects.select_related('customer', 'vehicle').all()
    return render(request, 'rentals/rental_history.html', {'rentals': rentals})


def return_vehicle(request, rental_id):
    """Mark vehicle as returned/available"""
    rental = get_object_or_404(Rental, pk=rental_id)
    rental.vehicle.available = True
    rental.vehicle.save()
    messages.success(request, f'Vehicle "{rental.vehicle.vehicle_name}" returned successfully!')
    return redirect('rental_history')


def dashboard(request):
    """Home dashboard with stats"""
    context = {
        'total_vehicles':   Vehicle.objects.count(),
        'available':        Vehicle.objects.filter(available=True).count(),
        'total_customers':  Customer.objects.count(),
        'total_rentals':    Rental.objects.count(),
        'recent_rentals':   Rental.objects.select_related('customer', 'vehicle').order_by('-rental_id')[:5],
    }
    return render(request, 'rentals/dashboard.html', context)
