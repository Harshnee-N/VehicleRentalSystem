# 🚗 Vehicle Rental System

A full-stack Vehicle Rental Management System developed using **Django**, **Django REST Framework**, **HTML**, **CSS**, and **MySQL**.

The system allows administrators to manage vehicles, customers, rentals, and returns through a web interface while also providing RESTful APIs for backend integration.

---

## 📖 Project Overview

This project is a redesigned version of a previous Python + SQL application.

The original console-based implementation has been transformed into a modern Django web application with:

- Dynamic web pages
- Database-driven operations
- REST APIs
- Responsive user interface

The application simplifies vehicle rental operations by managing vehicles, customers, rental records, billing, and vehicle availability.

---

# Features

## Vehicle Management

- Add new vehicles
- View available vehicles
- Store rental price per day
- Track vehicle availability

## Customer Management

- Register customers
- View customer records

## Rental Management

- Rent available vehicles
- Automatic rental bill calculation
- Update vehicle availability after rental
- Return rented vehicles
- View complete rental history

## Dashboard

- Central dashboard for navigation
- Quick access to all modules

## REST APIs

The project also provides REST API endpoints using Django REST Framework.

Available APIs include:

- Vehicles API
- Customers API
- Rental History API
- Rent Vehicle API

---

# Tech Stack

| Technology | Usage |
|------------|-------|
| Python | Backend Programming |
| Django | Web Framework |
| Django REST Framework | REST APIs |
| HTML5 | Frontend |
| CSS3 | Styling |
| MySQL | Database |
| Git | Version Control |
| GitHub | Repository Hosting |

---

# Project Structure

```
VehicleRentalSystem
│
├── vehicle_rental_django
│
├── rentals
│   ├── models.py
│   ├── views.py
│   ├── api_views.py
│   ├── serializers.py
│   ├── api_urls.py
│   ├── urls.py
│   ├── templates
│   └── migrations
│
├── vehicle_rental_project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# Database Design

The application uses three main entities:

- Vehicle
- Customer
- Rental

Relationships:

- One customer can rent multiple vehicles.
- One vehicle can have multiple rental records over time.
- Rental acts as the relationship between Customer and Vehicle.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Harshnee-N/VehicleRentalSystem.git
```

## Navigate

```bash
cd VehicleRentalSystem
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure MySQL Database

Update your database credentials inside:

```
vehicle_rental_project/settings.py
```

## Apply Migrations

```bash
python manage.py migrate
```

## Run Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

# Author

**Harshnee N**

GitHub:
https://github.com/Harshnee-N

---

# License

This project is developed for educational purposes.
