FROM python:2.7-slim

WORKDIR /app
ADD . /app

RUN pip install cqlsh
CMD [ "cqlsh", "172.20.0.2", "--cqlversion=3.4.4", "-f", "prepare.cql" ]