.PHONY : install compose kubernetes tests consumer webserver cassandra clear_consumer clear_webserver clear_all thrift_for_consumer thrift_for_webserver consumer_image webserver_image

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
	service cassandra start
	cd cassandra-prepare && cqlsh -f prepare.cql
	
consumer_image: thrift_for_consumer
	docker build -t kafka-consumer -f consumer/Dockerfile ./consumer && \
	docker tag kafka-consumer artlitvinov/kafka-consumer:latest

webserver_image: thrift_for_webserver
	docker build -t kafka-webserver -f webserver/Dockerfile ./webserver && \
	docker tag kafka-webserver artlitvinov/kafka-webserver:latest

cassandra_prepare_image:
	docker build -t cassandra-prepare -f cassandra-prepare/Dockerfile ./cassandra-prepare && \
	docker tag cassandra-prepare artlitvinov/cassandra-prepare:latest

compose: thrift_for_consumer thrift_for_webserver
	docker-compose down --remove-orphans
	docker-compose up --build

kubernetes:
	kubectl create --save-config -f kubernetes/cassandra-service.yaml
	kubectl create --save-config -f kubernetes/local-volumes.yaml
	kubectl create --save-config -f kubernetes/cassandra-statefulset.yaml
	kubectl create --save-config -f kubernetes/cassandra-prepare-job.yaml

	kubectl create --save-config -f kubernetes/kafka-service.yaml
	kubectl create --save-config -f kubernetes/kafka-deployment.yaml

	kubectl create --save-config -f kubernetes/webserver-service.yaml
	kubectl create --save-config -f kubernetes/webserver-deployment.yaml

	kubectl create --save-config -f kubernetes/consumer-deployment.yaml
	