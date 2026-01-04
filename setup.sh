#!/bin/bash

echo "======================================"
echo "CRM System - Quick Setup Script"
echo "======================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed!"
    echo "Please install Python 3.8 or higher first."
    exit 1
fi

echo "✓ Python 3 is installed"

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo ""
echo "Setting up database..."
python manage.py makemigrations
python manage.py migrate

# Create media directories
echo ""
echo "Creating media directories..."
mkdir -p media/customer_images
mkdir -p media/profile_images

# Completion message
echo ""
echo "======================================"
echo "Setup Complete!"
echo "======================================"
echo ""
echo "Next steps:"
echo "1. Create admin user manually:"
echo "   python manage.py createsuperuser"
echo "2. Start the server:"
echo "   python manage.py runserver"
echo ""
echo "Then open your browser and navigate to:"
echo "   http://127.0.0.1:8000/"
echo ""
echo "======================================"
