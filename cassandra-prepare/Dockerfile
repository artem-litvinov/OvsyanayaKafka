FROM python:2.7-slim

RUN pip install cqlsh

ENV CASSANDRA_HOST 127.0.0.1

WORKDIR /app
ADD . /app

CMD cqlsh ${CASSANDRA_HOST} --cqlversion="3.4.4" -f prepare.cql