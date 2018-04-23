#!/usr/bin/env sh
# Generate .env if necessary
python genenv.py

# Populate DB schema with any required changes
python manage.py migrate

# Start dev web server
python manage.py runserver 0.0.0.0:8000
