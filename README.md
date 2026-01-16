Calendar Backend API

A Django REST API for managing users and calendar appointments with JWT authentication, role-based access, and appointment background notifications via Celery + Redis.

Tech Stack

Python 3.11, Django 5.2

Django REST Framework, JWT (simplejwt)

PostgreSQL, Celery + Redis

drf-spectacular (Swagger / Redoc)

Docker & Docker Compose

Setup

Clone repo and create virtual environment:

git clone https://github.com/Soumendra045/calendar-backend.git
cd calendar-backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Configure .env with DB and SECRET_KEY

Run Docker Compose:

docker compose up --build
docker compose exec web python manage.py migrate


Create superuser (admin):

docker compose exec web python manage.py createsuperuser

JWT Auth Flow

Register: POST /api/auth/register/

Login: POST /api/auth/login/ → returns access & refresh tokens

Use header for protected endpoints: Authorization: Bearer <access_token>

API Endpoints

Appointments (USER)

POST /api/appointments/ → create

GET /api/appointments/mine/ → list own

Appointments (ADMIN)

GET /api/appointments/all/ → list all

Users (ADMIN)

GET /api/users/ → list all users