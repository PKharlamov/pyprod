FROM python:3.11-buster

WORKDIR /pyprod/

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        git \
        python3-pip \
        python3-dev \
        libpq-dev
#       postgresql-contrib \

COPY requirements.pip requirements.pip
RUN pip install -r requirements.pip
ENV PYTHONUNBUFFERED=1

EXPOSE 8000
