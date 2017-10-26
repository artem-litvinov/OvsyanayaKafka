FROM python:3.5.2

RUN pip install thrift aiohttp aiokafka aiocassandra aiohttp_jinja2 prometheus_client

ENV KAFKA_HOST 0.0.0.0
ENV WEBSERVER_PORT 5000
ENV CASSANDRA_HOST 127.0.0.1

WORKDIR /app
ADD . /app

EXPOSE 5000
EXPOSE 8008
CMD python app.py