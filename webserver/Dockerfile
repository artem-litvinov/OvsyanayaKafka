FROM python:2.7-slim

WORKDIR /app
ADD . /app
RUN pip install flask
RUN pip install cassandra-driver
EXPOSE 5000
CMD ["python", "app.py"]