import os, sys
import time
from thrift.TSerialization import serialize

from client_base import Client_Base
from kafka import KafkaProducer
try:
    sys.path.append('./gen-py')
    from kafka_message.ttypes import Kafka_Message
except ImportError:
    sys.path.append(os.path.abspath(os.path.join('common','gen-py')))
    from kafka_message.ttypes import Kafka_Message


class Producer(Client_Base):
    def __connect(self, topic, data):
        try:
            self.producer = KafkaProducer(bootstrap_servers=self.server())
            self.send(topic, data)
        except BaseException as e:
            print e
            time.sleep(1)
            print "connecting..."
            self.__connect(topic, data)

    def send(self, topic, data):
        if hasattr(self, 'producer'):
            try:
                serialized_data = serialize(Kafka_Message(data))
                self.producer.send(topic, serialized_data)
            except BaseException as e:
                print e
                self.producer.send(topic, data)
        else:
            self.__connect(topic, data)

if __name__ == "__main__":
    producer = Producer('34.214.200.68', '9092')
    producer.send('test-topic', '1507300909746')
    time.sleep(1)
