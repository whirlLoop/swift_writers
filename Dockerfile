# pull base image
FROM python:3.9.0

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
COPY Pipfile Pipfile.lock ./
RUN pip install --upgrade pip pipenv && pipenv install --system

# create directory for the app user
RUN mkdir -p /home/app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/swift_writers
RUN mkdir $APP_HOME

# copy project
COPY ./app .

# copy entrypoint-dev.sh
COPY ./scripts/entrypoint.dev.sh $APP_HOME
RUN chmod u+x $APP_HOME/entrypoint.dev.sh

RUN ls $APP_HOME

# start app
ENTRYPOINT ["/home/app/swift_writers/entrypoint.dev.sh"]