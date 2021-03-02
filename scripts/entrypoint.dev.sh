#!/bin/sh

# test redis
# redis-cli -h redis -p 6379 ping

# prepare application
python manage.py set_essays_cache
python manage.py set_academic_levels_cache
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
exec "$@"