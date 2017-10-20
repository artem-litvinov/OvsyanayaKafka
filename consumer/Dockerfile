FROM python:3.5.2

RUN pip install thrift aiokafka aiocassandra boto3

ENV KAFKA_HOST 0.0.0.0
ENV CASSANDRA_HOST 0.0.0.0

WORKDIR /app
ADD . /app

CMD python -u init_consumer.py
