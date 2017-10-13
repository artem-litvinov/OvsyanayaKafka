FROM python:2.7-slim

RUN pip install thrift kafka-python cassandra-driver boto3

ENV KAFKA_HOST 0.0.0.0
ENV CASSANDRA_HOST 0.0.0.0

WORKDIR /app
ADD . /app

CMD python -u init_consumer.py
