import options
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=options.host + ':' + options.port)

print "Producer started\n"
for _ in range(100):
    producer.send(options.topic, b'some_message_bytes')
