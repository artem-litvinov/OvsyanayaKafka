import os
import time
from kafka import KafkaProducer
from thrift.TSerialization import serialize
from kafka_message.ttypes import KafkaMessage


class Producer():
    def __init__(self, host='localhost', port='9092'):
        self.__address = "%s:%s" % (host, port)
        self.producer = KafkaProducer(bootstrap_servers=self.__address)

    def send(self, topic, data):
        serialized_data = serialize(KafkaMessage(data))
        self.producer.send(topic, serialized_data)


if __name__ == "__main__":
    try:
        KAFKA_HOST = os.environ['KAFKA_HOST']
    except KeyError as err:
        print(err, "Please set KAFKA_HOST environment variable")
        raise
    producer = Producer(KAFKA_HOST, '9092')
    producer.send('test-topic', '1507300909746')
    time.sleep(1)
