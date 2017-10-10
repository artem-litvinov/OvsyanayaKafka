.PHONY : install tests consumer webserver cassandra clear_consumer clear_webserver clear_all thrift_for_consumer thrift_for_webserver

install:
	pipenv install

thrift_for_consumer:
	thrift -r -out consumer --gen py thrift/kafka_message.thrift

thrift_for_webserver:
	thrift -r -out webserver --gen py thrift/kafka_message.thrift

tests: thrift_for_consumer thrift_for_webserver
	pipenv install -d
	pipenv run py.test -s -v

consumer: thrift_for_consumer
	cd consumer && pipenv run python init_consumer.py port=9092 host=34.214.200.68

webserver: thrift_for_webserver
	cd webserver && python app.py

cassandra:
	docker build -t kafka_cassandra -f cassandra/Dockerfile ./cassandra

build_and_push_consumer:
	sudo docker build -t kafka_consumer -f consumer/Dockerfile . && \
	sudo docker tag kafka_consumer artlitvinov/akvelon:kafka_consumer && \
	sudo docker push artlitvinov/akvelon:kafka_consumer
