FROM python:2.7-slim

WORKDIR /app
ADD /common/. /app
ADD /subscriber/init_consumer.py /app

# RUN pip install boto3
RUN pip install thrift
RUN pip install kafka-python
RUN pip install cassandra-driver
RUN apt-get update

RUN apt-get install thrift-compiler
RUN thrift -r --gen py kafka_message.thrift

CMD ["python", "init_consumer.py", "port=9092", "host=34.214.200.68"]
