#!/bin/sh
# redis-server  --bind 0.0.0.0
docker run -d -p 6379:6379 redis-server --bind 0.0.0.0
sleep 5
python manage.py set_essays_cache
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
gunicorn -b 0.0.0.0:8000 swift_writers.wsgi:application --timeout 90
exec "$@"
