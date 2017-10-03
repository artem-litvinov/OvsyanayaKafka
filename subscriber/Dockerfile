FROM python:2.7-slim

WORKDIR /app
ADD /common/. /app
ADD /subscriber/init_consumer.py /app

RUN pip install boto3
RUN pip install kafka-python
RUN pip install cassandra-driver
RUN apt-get update

RUN apt-get install thrift-compiler
RUN thrift -r --gen py kafka_message.thrift

RUN apt-get install wget -y
RUN apt-get install unzip -y

RUN wget https://pypi.python.org/packages/a3/ea/84a41e03f1ab14fb314c8bcf1c451090efa14c5cdfb9797d1079f502b54e/thrift-0.10.0.zip
RUN unzip thrift-0.10.0.zip
WORKDIR thrift-0.10.0
RUN python setup.py install
WORKDIR /app
RUN rm -rf thrift-0.10.0 thrift-0.10.0.zip

CMD ["python", "init_consumer.py", "port=9092", "host=34.214.200.68"]
