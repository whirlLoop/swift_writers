#!/bin/sh
python manage.py set_essays_cache
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
gunicorn -b 0.0.0.0:8000 swift_writers.wsgi:application --timeout 90
exec "$@"
