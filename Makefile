.PHONY: install thrift test

install:
	sudo apt update
	sudo -H pip install pipenv
	sudo apt-get install python cassandra thrift-compiler
	pipenv install
thrift:
	thrift -r -out common --gen py common/kafka_message.thrift
test:
	cp -r common/kafka_message webserver/
	py.test -s -v tests
	rm -r webserver/kafka_message
	rm -r tests/__pycache__
