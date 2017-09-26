FROM python:2.7-slim

WORKDIR /app
ADD . /app

RUN pip install kafka-python
RUN python init_consumer.py
