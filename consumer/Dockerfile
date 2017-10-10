FROM python:2.7-slim

WORKDIR /app
ADD . /app
ADD ./thrift/kafka_message.thrift /app

RUN pip install boto3 flask thrift kafka-python cassandra-driver
RUN apt-get update

RUN apt-get install thrift-compiler
RUN thrift -r --gen py kafka_message.thrift

CMD ["python", "init_consumer.py"]
