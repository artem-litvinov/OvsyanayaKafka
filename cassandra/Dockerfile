FROM cassandra

WORKDIR /cassandra
ADD ./prepare.cql /cassandra

RUN echo "deb http://www.apache.org/dist/cassandra/debian 311x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
RUN curl https://www.apache.org/dist/cassandra/KEYS | sudo apt-key add -
RUN sudo apt-get update
RUN sudo apt-get install cassandra -y
RUN sudo service cassandra start
RUN cqlsh -f ./prepare.cql