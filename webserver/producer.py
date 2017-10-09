import time
from kafka import KafkaProducer
from thrift.TSerialization import serialize
from .kafka_message.ttypes import Kafka_Message


class Producer():
    def __init__(self, host='localhost', port='9092'):
        self.__address = "%s:%s" % (host, port)
        self.producer = KafkaProducer(bootstrap_servers=self.__address)

    def send(self, topic, data):
        serialized_data = serialize(Kafka_Message(data))
        self.producer.send(topic, serialized_data)

if __name__ == "__main__":
    producer = Producer('34.214.200.68', '9092')
    producer.send('test-topic', '1507300909746')
    time.sleep(1)
