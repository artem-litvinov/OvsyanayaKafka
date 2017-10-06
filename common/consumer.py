import sys
import json
import time
import thread

from client_base import Client_Base
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

class Consumer(Client_Base):
    def __connect(self):
        self.consumer = KafkaConsumer(bootstrap_servers=self.server())
    
    def try_connect(self):
        try: 
            self.__connect()
            return True
        except NoBrokersAvailable as e:
            print e
            return False 

    def subscribe(self, topic):
        if hasattr(self, 'consumer') == False:
            while self.try_connect() != True:
                time.sleep(1)

        try:
            self.consumer.subscribe(topic)
        except BaseException as e:
            print e

    def get_message_generator(self, topic = None):
            if hasattr(self, 'consumer') == False and topic is not None:
                self.subscribe(topic)

            if hasattr(self, 'consumer') == False and topic is None:
                raise RuntimeError('You have no available consumer yet!')

            return self.consumer
def callback(msg):
    print msg

if __name__ == "__main__":
    consumer = Consumer('34.214.200.68', '9092')
    gen = consumer.get_message_generator('test-topic')
    for m in gen:
        print m