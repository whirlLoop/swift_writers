#!/bin/sh
redis-server /etc/redis/redis.conf protected-mode no
# test redis
redis-cli -h localhost -p 6379 ping
python manage.py set_essays_cache
python manage.py set_academic_levels_cache
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
gunicorn -b 0.0.0.0:8000 swift_writers.wsgi:application --timeout 90
exec "$@"
