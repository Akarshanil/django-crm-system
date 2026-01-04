@echo off
echo ======================================
echo CRM System - Quick Setup Script
echo ======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed!
    echo Please install Python 3.8 or higher first.
    pause
    exit /b 1
)

echo Python is installed
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Run migrations
echo.
echo Setting up database...
python manage.py makemigrations
python manage.py migrate

REM Create media directories
echo.
echo Creating media directories...
if not exist "media\customer_images" mkdir media\customer_images
if not exist "media\profile_images" mkdir media\profile_images

echo.
echo ======================================
echo Setup Complete!
echo ======================================
echo.
echo Next steps:
echo 1. Create admin user:
echo    python manage.py createsuperuser
echo.
echo 2. Start the server:
echo    python manage.py runserver
echo.
echo Then open:
echo http://127.0.0.1:8000/
echo.
echo ======================================
pause
