# Customer Management System

A simple web-based CRM application built with Django.

## Features
- User authentication (Login / Logout)
- Admin dashboard
- Customer CRUD operations
- Profile management
- Django messages for alerts
- Bootstrap-based UI

## Tech Stack
- Python
- Django
- SQLite
- Bootstrap

### 2. Run the setup script (optional)
- On **Windows**: double-click `setup.bat` or run in terminal:
  ```bash
  setup.bat
- On **Linux/macOS**: run setup.sh:
    bash setup.sh

## Setup Instructions

1. **Download the code**  
   Clone the repository or download the ZIP from GitHub and extract it.


2. **Create a virtual environment**  
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   # or on Linux/macOS
   # source venv/bin/activate
3. **Install dependencies**
    pip install -r requirements.txt
4. **Run migrations**
    python manage.py migrate
5. **Create a superuser**
    python manage.py createsuperuser
6. **Run the development server**
    python manage.py runserver
7. **Open your browser and navigate to:**
    http://127.0.0.1:8000/
    

