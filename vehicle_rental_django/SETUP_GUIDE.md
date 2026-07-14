# Vehicle Rental System — Django Setup Guide

## Project Structure

```
vehicle_rental_django/
│
├── manage.py
├── requirements.txt
│
├── vehicle_rental_project/
│   ├── __init__.py
│   ├── settings.py          ← DB config here
│   ├── urls.py
│   └── wsgi.py
│
└── rentals/                 ← Main Django app
    ├── models.py            ← Vehicle, Customer, Rental models
    ├── views.py             ← Web UI views
    ├── api_views.py         ← REST API views
    ├── serializers.py       ← DRF serializers
    ├── urls.py              ← Web UI routes
    ├── api_urls.py          ← API routes
    └── templates/rentals/
        ├── base.html
        ├── dashboard.html
        ├── vehicle_list.html
        ├── add_vehicle.html
        ├── customer_list.html
        ├── add_customer.html
        ├── rent_vehicle.html
        └── rental_history.html
```

---

## Step 1 — Install Dependencies

```bash
pip install -r requirements.txt
```

> If mysqlclient fails on Windows, install it via:
> `pip install mysqlclient‑2.x.x‑cp311‑win_amd64.whl` from https://www.lfd.uci.edu/~gohlke/pythonlibs/

---

## Step 2 — Setup MySQL Database

Your original `database.sql` already creates the database and tables.
Run it in MySQL Workbench or terminal:

```bash
mysql -u root -p < database.sql
```

The Django models use `db_table` to point to your **existing tables** — no data loss!

---

## Step 3 — Check Database Password

Open `vehicle_rental_project/settings.py` and confirm:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vehicle_rental',
        'USER': 'root',
        'PASSWORD': 'MySqL@123',   # ← update if different
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## Step 4 — Run Migrations

Since your tables already exist, run fake migrations:

```bash
python manage.py migrate --fake-initial
```

Or if starting fresh:

```bash
python manage.py migrate
```

---

## Step 5 — Create Admin User (Optional)

```bash
python manage.py createsuperuser
```

---

## Step 6 — Run the Server

```bash
python manage.py runserver
```

Open browser: **http://127.0.0.1:8000/**

---

## Web UI Pages

| Page             | URL                      |
|------------------|--------------------------|
| Dashboard        | http://127.0.0.1:8000/   |
| Vehicle List     | http://127.0.0.1:8000/vehicles/      |
| Add Vehicle      | http://127.0.0.1:8000/vehicles/add/  |
| Customer List    | http://127.0.0.1:8000/customers/     |
| Add Customer     | http://127.0.0.1:8000/customers/add/ |
| Rent Vehicle     | http://127.0.0.1:8000/rentals/rent/  |
| Rental History   | http://127.0.0.1:8000/rentals/       |

---

## REST API Endpoints

| Method | Endpoint                          | Description              |
|--------|-----------------------------------|--------------------------|
| GET    | /api/vehicles/                    | List available vehicles  |
| POST   | /api/vehicles/                    | Add new vehicle          |
| GET    | /api/vehicles/<id>/               | Get vehicle detail       |
| DELETE | /api/vehicles/<id>/               | Delete vehicle           |
| GET    | /api/customers/                   | List all customers       |
| POST   | /api/customers/                   | Add new customer         |
| GET    | /api/customers/<id>/              | Get customer detail      |
| GET    | /api/rentals/                     | Full rental history      |
| POST   | /api/rentals/rent/                | Rent a vehicle           |
| POST   | /api/rentals/<id>/return/         | Return a vehicle         |

### Example API Call — Rent a Vehicle

```bash
POST http://127.0.0.1:8000/api/rentals/rent/
Content-Type: application/json

{
    "customer_id": 1,
    "vehicle_id": 2,
    "days_rented": 3
}
```

Response:
```json
{
    "message": "Vehicle rented successfully!",
    "rental_id": 1,
    "customer": "Ravi Kumar",
    "vehicle": "Honda City",
    "days_rented": 3,
    "total_amount": "₹7500.0"
}
```

---

## How Your Original Code Maps to Django

| Original File  | Django Equivalent              |
|----------------|-------------------------------|
| `Vehicle.py`   | `models.py → Vehicle model`   |
| `customer.py`  | `models.py → Customer model`  |
| `rental.py`    | `models.py → Rental model`    |
| `db.py`        | `settings.py → DATABASES`     |
| `main.py`      | `views.py + api_views.py`     |
| `database.sql` | `models.py + migrations`      |

---

## Common Errors & Fixes

**Error:** `django.db.utils.OperationalError: (1045, "Access denied")`
**Fix:** Update PASSWORD in settings.py

**Error:** `No module named 'MySQLdb'`
**Fix:** `pip install mysqlclient`

**Error:** `Table already exists`
**Fix:** Use `python manage.py migrate --fake-initial`
