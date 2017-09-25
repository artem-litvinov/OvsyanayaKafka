import options
from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers=options.host + ':' + options.port)
consumer.subscribe(options.topic)

print "Consumer started\n"
for msg in consumer:
    print(msg.value)
