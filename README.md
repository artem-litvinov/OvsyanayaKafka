# OvsyanayaKafka

## Amazon
Create EC2 Ubuntu instance as described [here]()

## Docker
Follow [Docker installation instructions](http://asd.com)

## Kafka
Run

    sudo docker run -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST='EC2 IP' --env ADVERTISED_PORT=9092 --env KAFKA_HEAP_OPTS=Xms256MB,Xmx256MB spotify/kafka

##Consumer
Create another EC2 instance, then run

    sudo docker run -p 9092:9092 akvelon/kafka_consumer