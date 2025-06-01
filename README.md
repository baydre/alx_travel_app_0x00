# alx_travel_app_0x00

## Setup Instructions

1. Clone the repository
2. Create a virtual environment and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations and seed data:
    ```python
    python manage.py makemigrations
    python manage.py migrate
    python manage.py seed
    ```
4. Run the server:
    ```python
    python manage.py runserver
    ```
## API Endpoints (WIP)
- `/api/listings/` – List all listings

- `/api/bookings/` – List all bookings

## Seeder Command

- To populate the database with sample data, run:
    ```python
    python manage.py seed
    ```
