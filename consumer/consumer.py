import sys
import json
import time
import thread

from kafka import KafkaConsumer

class Consumer():
    def __init__(self, host='localhost', port='9092'):
        self.__address = "%s:%s" % (host, port)
        self.consumer = KafkaConsumer(bootstrap_servers=self.__address)

    def subscribe(self, topic):
        self.consumer.subscribe(topic)

    def messages(self, topic = None):
        if topic is None:
            raise RuntimeError('You have no available consumer yet!')

        self.subscribe(topic)
        return self.consumer


if __name__ == "__main__":
    consumer = Consumer('34.214.200.68', '9092')
    for message in consumer.messages('test-topic'):
        print message