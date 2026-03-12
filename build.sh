#!/bin/bash

# Build script for GroceryBud Django REST Framework application
# Author: Priyanshu Verma
# Description: Automated build and deployment setup

set -o errexit

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Running database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!"
echo "Author: Priyanshu Verma"
