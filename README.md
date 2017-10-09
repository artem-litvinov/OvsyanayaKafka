# OvsyanayaKafka

## Installation

    make install

## Testing

    make tests

## Launch Amazon EC2 Instance
- Create EC2 Ubuntu instance as described [here](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance)
- Go to security group and create "Inbound" rule that will open 9092 port to all sources.
- Connect to instance and follow [Docker installation instructions](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/)

## Kafka
[Launch](https://github.com/litvinovArt/OvsyanayaKafka#launch-amazon-ec2-instance) Kafka instance, connect to it, then run

    sudo docker run -p 2181:2181 -p 9092:9092 \
        --env ADVERTISED_HOST='EC2 IP' \
        --env ADVERTISED_PORT=9092 \
        --env KAFKA_HEAP_OPTS=Xms256MB,Xmx256MB \
        spotify/kafka

## Consumer
[Launch](https://github.com/litvinovArt/OvsyanayaKafka#launch-amazon-ec2-instance) Consumer instance, connect to it, then run

    sudo docker run -it artlitvinov/akvelon:kafka_consumer

## Producer
To start Producer you can run this on your local machine

    sudo docker run -it artlitvinov/akvelon:kafka_producer
