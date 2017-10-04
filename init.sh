sudo docker stop kafka_consumer kafka_cassandra kafka_webserver
sudo docker rm kafka_consumer kafka_cassandra kafka_webserver
sudo docker run --name kafka_cassandra -m 2g --memory-swap -1 -d artlitvinov/akvelon:kafka_cassandra
cassandra_host=`docker inspect --format='{{ .NetworkSettings.IPAddress }}' kafka_cassandra`
echo loading...
sleep 70
sudo docker run -it --link kafka_cassandra --rm artlitvinov/akvelon:kafka_cassandra  sh -c 'exec cqlsh '$cassandra_host' -f prepare.cql'
sudo docker run --name kafka_webserver -p 5000:5000 -it artlitvinov/akvelon:kafka_webserver &
sudo docker run -it artlitvinov/akvelon:kafka_consumer