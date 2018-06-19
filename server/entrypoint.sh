#!/bin/sh
cd /live-location-tracker
echo "Waiting so that the DB is up and running"
sleep 40
python manage.py makemigrations --settings=livelocationtracker.prod_settings
python manage.py migrate --settings=livelocationtracker.prod_settings
#export DJANGO_SETTINGS_MODULE=livelocationtracker.docker-settings
#python manage.py createsuperuser --username=admin --email=admin@example.com
#export DJANGO_SETTINGS_MODULE=ivelocationtracker.prod_settings
#gunicorn -b :8000 livelocationtracker.wsgi
python manage.py runserver --settings=livelocationtracker.prod_settings 0.0.0.0:8000