#!/bin/bash

# Veritabanı migrations'larını çalıştır
python manage.py migrate

# Gunicorn ile uygulamayı başlat
exec gunicorn BookManagementSystem.wsgi:application --bind 0.0.0.0:8000