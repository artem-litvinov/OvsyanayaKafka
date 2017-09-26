FROM python:2.7-slim

WORKDIR /app
ADD . /app

RUN pip install kafka-python
CMD ['start.sh']
