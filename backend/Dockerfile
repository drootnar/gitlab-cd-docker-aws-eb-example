FROM python:3.5.2

MAINTAINER Kamil Rogalski <drootnar@gmail.com>

RUN mkdir -p /app
ADD . /app

WORKDIR /app

CMD bash -c "pip install -r requirements.txt && gunicorn backend:app -w 2 --bind 0.0.0.0:8000"