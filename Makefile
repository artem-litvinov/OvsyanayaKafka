.PHONY : install compose tests monitoring consumer webserver cassandra clear_consumer clear_webserver clear_all thrift_for_consumer thrift_for_webserver consumer_image webserver_image

install:
	pipenv install

thrift_for_consumer:
	thrift -r -out consumer --gen py thrift/kafka_message.thrift

thrift_for_webserver:
	thrift -r -out webserver/tools --gen py thrift/kafka_message.thrift

tests: thrift_for_consumer thrift_for_webserver
	pipenv --three
	pipenv install
	pipenv run pytest -s -v

consumer: thrift_for_consumer
	cd consumer && pipenv run python init_consumer.py

webserver: thrift_for_webserver
	cd webserver && pipenv run python app.py

cassandra:
	service cassandra start
	cd cassandra && cqlsh -f prepare.cql

consumer_image: thrift_for_consumer
	docker build -t kafka_consumer -f consumer/Dockerfile ./consumer

webserver_image: thrift_for_webserver
	docker build -t kafka_webserver -f webserver/Dockerfile ./webserver

cassandra_image:
	docker build -t kafka_cassandra -f cassandra/Dockerfile ./cassandra

compose: thrift_for_consumer thrift_for_webserver
	docker-compose down --remove-orphans
	docker-compose up --build

monitoring:
	docker-compose -f monitoring/docker-compose.yml up