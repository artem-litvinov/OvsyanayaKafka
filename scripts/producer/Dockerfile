FROM python:2.7-slim

WORKDIR /app
ADD . /app

RUN pip install kafka-python
EXPOSE 9092
CMD ["python", "init_producer.py", "port=9092", "host=34.214.200.68"]
