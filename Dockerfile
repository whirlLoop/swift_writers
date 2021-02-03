# pull base image
FROM python:3.7.6

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
COPY Pipfile Pipfile.lock ./
RUN pip install --upgrade pip pipenv && pipenv install --system

# copy project
COPY ./app .

CMD python manage.py makemigrations; python manage.py migrate; python manage.py dev_admin; python manage.py runserver 0.0.0.0:8000
