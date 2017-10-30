FROM python:2.7-slim

RUN apt-get update && apt-get install -yq netcat
WORKDIR /app
ADD . /app

RUN pip install cqlsh
CMD cqlsh ${CASSANDRA_HOST} --cqlversion="3.4.4" -f prepare.cql
