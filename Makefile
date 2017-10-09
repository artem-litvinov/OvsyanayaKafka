install:
	sudo apt update
	sudo apt-get install thrift-compiler python cassandra
	sudo -H pip install pipenv
	pipenv install
thrift:
	thrift -r -out common --gen py common/kafka_message.thrift
test:
	py.test -s -v tests
