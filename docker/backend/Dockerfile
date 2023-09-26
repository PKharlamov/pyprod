FROM python:3.11-buster

WORKDIR /pyprod/

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        git \
        python3-pip \
        python3-dev \
        libpq-dev

COPY backend/requirements/requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r /tmp/requirements.txt

COPY ./docker/backend/docker_entrypoint.sh /docker_entrypoint.sh
COPY ./docker/backend/docker_bin/* /docker_bin/
RUN chmod +x /docker_entrypoint.sh \
    && chmod +x /docker_bin/* \
    && true


ENV PYTHONUNBUFFERED=1

EXPOSE 8000

WORKDIR /app/backend/
ADD backend .
ENTRYPOINT /docker_entrypoint.sh
