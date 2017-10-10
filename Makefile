.PHONY : install tests consumer webserver cassandra clear_consumer clear_webserver clear_all thrift_for_consumer thrift_for_webserver

install:
	sudo apt update
	sudo -H pip install pipenv
	sudo apt-get install python cassandra thrift-compiler
	pipenv install

thrift_for_consumer:
	thrift -r -out consumer --gen py thrift/kafka_message.thrift

thrift_for_webserver:
	thrift -r -out webserver --gen py thrift/kafka_message.thrift

tests: thrift_for_consumer thrift_for_webserver
	py.test -s -v
	make clear_consumer
	make clear_webserver
	make clear_tests

consumer: thrift_for_consumer
	cd consumer && python init_consumer.py port=9092 host=34.214.200.68

webserver: thrift_for_webserver
	cd webserver && python app.py

cassandra:
	sudo service cassandra start
	cd cassandra && sudo cqlsh -f prepare.cql

build_and_push_consumer:
	sudo docker build -t kafka_consumer -f consumer/Dockerfile . && \
	sudo docker tag kafka_consumer artlitvinov/akvelon:kafka_consumer && \
	sudo docker push artlitvinov/akvelon:kafka_consumer

clear_consumer:
	cd consumer && rm -r ./kafka_message ./*.pyc

clear_webserver:
	cd webserver && rm -r ./kafka_message ./*.pyc

clear_tests:
	cd tests && rm -r ./__pycache__ ./*.pyc