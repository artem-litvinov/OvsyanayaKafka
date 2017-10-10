import os
from kafka import KafkaConsumer

KAFKA_HOST = os.environ['KAFKA_HOST']


class Consumer():
    def __init__(self, host='localhost', port='9092'):
        self.__address = "%s:%s" % (host, port)
        self.consumer = KafkaConsumer(bootstrap_servers=self.__address)

    def subscribe(self, topic):
        self.consumer.subscribe(topic)

    def messages(self, topic = None):
        if topic is not None:
            self.subscribe(topic)

        return self.consumer


if __name__ == "__main__":
    consumer = Consumer(KAFKA_HOST, '9092')
    for message in consumer.messages('test-topic'):
        print message