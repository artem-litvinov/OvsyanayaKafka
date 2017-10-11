.PHONY : install tests consumer webserver cassandra clear_consumer clear_webserver clear_all thrift_for_consumer thrift_for_webserver consumer_image webserver_image

install:
	pipenv install

environment_variables:
	export WEBSERVER_PORT=5000
	export KAFKA_HOST=34.214.200.68
	export CASSANDRA_HOST=172.17.0.2

thrift_for_consumer:
	thrift -r -out consumer --gen py thrift/kafka_message.thrift

thrift_for_webserver:
	thrift -r -out webserver --gen py thrift/kafka_message.thrift

tests: thrift_for_consumer thrift_for_webserver
	pipenv install -d
	pipenv run py.test -s -v

consumer: thrift_for_consumer
	cd consumer && pipenv run python init_consumer.py

webserver: thrift_for_webserver
	cd webserver && pipenv run python app.py

cassandra:
	sudo service cassandra start
	cd cassandra && sudo cqlsh -f prepare.cql
	
consumer_image: thrift_for_consumer
	sudo docker build -t kafka_consumer -f consumer/Dockerfile ./consumer

webserver_image: thrift_for_webserver
	sudo docker build -t kafka_webserver -f webserver/Dockerfile ./webserver

cassandra_image:
	sudo docker build -t kafka_cassandra -f cassandra/Dockerfile ./cassandra