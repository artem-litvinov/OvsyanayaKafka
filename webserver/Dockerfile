FROM python:2.7-slim

RUN pip install flask thrift kafka-python cassandra-driver

ENV KAFKA_HOST 0.0.0.0
ENV WEBSERVER_PORT 5000
ENV CASSANDRA_HOST 127.0.0.1

WORKDIR /app
ADD . /app

EXPOSE 5000
CMD ["python", "app.py"]