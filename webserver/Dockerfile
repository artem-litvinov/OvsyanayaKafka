FROM python:2.7-slim

WORKDIR /app
ADD webserver/. /app
ADD common/kafka_message.thrift /app

RUN pip install flask thrift kafka-python cassandra-driver

RUN apt-get update

RUN apt-get install thrift-compiler
RUN thrift -r --gen py kafka_message.thrift

EXPOSE 5000
CMD ["python", "app.py"]