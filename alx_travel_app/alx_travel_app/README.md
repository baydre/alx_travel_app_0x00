# ALX_TRAVEL_APP

A Django-based travel application for managing property listings and bookings.

## Features

- List travel properties (listings)
- Book properties (bookings)
- REST API endpoints for listings and bookings

## Project Structure

```
alx_travel_app/
├── manage.py
├── alx_travel_app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── requirement.txt
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
├── listings/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
│   └── migrations/
│       └── __init__.py
```

## Setup Instructions

1. **Clone the repository**

2. **Create a virtual environment and install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

3. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `/api/listings/` – List all listings
- `/api/bookings/` – List all bookings

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.
