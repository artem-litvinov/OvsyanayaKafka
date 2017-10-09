install:
	pipenv install
thrift:
	thrift -r -out common --gen py common/kafka_message.thrift
test:
	py.test -s -v tests
