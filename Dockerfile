FROM python:3.7.6-alpine3.11

# Set environment variables.
# PYTHONDONTWRITEBYTECODE prevents Python from writing pyc files to disc.
# PYTHONUNBUFFERED Prevents Python from buffering stdout and stderr.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app so any further instructions on the dockerfile
# occur within this directory.
RUN mkdir /app
WORKDIR /app

RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers
# Copy the requirements file into the image's filesystem at /app directory.
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /app/

# Install dependencies.
RUN pip install -r requirements.txt

# Copy the current directory contents into the image's filesystem at /app directory.
COPY . /app

# Create and switch to a user who will run our application instead of the root
# user (security measure applied in case the application is hacked).
RUN adduser -D runner
USER runner

