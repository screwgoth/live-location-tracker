#!/bin/sh
cd /live-location-tracker
echo "Waiting so that the DB is up and running"
sleep 40
python manage.py makemigrations
python manage.py migrate
#export DJANGO_SETTINGS_MODULE=livelocationtracker.docker-settings
#python manage.py createsuperuser --username=admin --email=admin@example.com
#gunicorn -b :8000 livelocationtracker.wsgi
python manage.py runserver 0.0.0.0:8000