FROM python:2.7-slim

WORKDIR /app
ADD webserver/app.py /app
ADD webserver/templates/. /app/templates
ADD common/kafka_common.py /app
ADD common/producer.py /app
ADD common/kafka_message.thrift /app

RUN pip install flask
RUN pip install thrift
RUN pip install kafka-python
RUN pip install cassandra-driver

RUN apt-get update

RUN apt-get install thrift-compiler
RUN thrift -r --gen py kafka_message.thrift

EXPOSE 5000
CMD ["python", "app.py"]