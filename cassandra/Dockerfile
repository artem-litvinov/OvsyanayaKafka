FROM ubuntu:latest

WORKDIR /cassandra
ADD cassandra/prepare.cql /cassandra

RUN echo "deb http://www.apache.org/dist/cassandra/debian 311x main" | tee -a /etc/apt/sources.list.d/cassandra.sources.list
RUN apt-get update
RUN apt-get install curl -y
RUN curl https://www.apache.org/dist/cassandra/KEYS | apt-key add -

RUN apt-get install cassandra -y --allow-unauthenticated

EXPOSE 9042
RUN service cassandra start
CMD ["cqlsh", "-f", "./prepare.cql"]
