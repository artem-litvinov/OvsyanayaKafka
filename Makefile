.PHONY : install thrift test consumer webserver clear_consumer clear_webserver cassandra

install:
	sudo apt update
	sudo -H pip install pipenv
	sudo apt-get install python cassandra thrift-compiler
	pipenv install

test:
	thrift -r -out consumer --gen py thrift/kafka_message.thrift
	thrift -r -out webserver --gen py thrift/kafka_message.thrift
	py.test -s -v tests
	rm -r tests/__pycache__

consumer:
	thrift -r -out consumer --gen py thrift/kafka_message.thrift
	cd consumer && python init_consumer.py port=9092 host=34.214.200.68

webserver:
	thrift -r -out webserver --gen py thrift/kafka_message.thrift
	cd webserver && python app.py

clear_consumer:
	cd consumer && rm -r ./kafka_message ./__init__.py **/*.pyc

clear_webserver:
	cd webserver && rm -r ./kafka_message ./__init__.py **/*.pyc

cassandra:
	sudo service cassandra start
	cd cassandra && sudo cqlsh -f prepare.cql

clear_all: clear_consumer clear_webserver