import sys
import time
from thrift.TSerialization import serialize

from kafka_common import AKafkaCommon
from kafka import KafkaProducer
sys.path.append('./gen-py')
from kafka_message.ttypes import Kafka_Message


class AProducer(AKafkaCommon):
    def __connect(self, cb, topic, data):
        try:
            self.producer = KafkaProducer(bootstrap_servers=self.server())
            cb(topic, data)
        except BaseException as e:
            print e
            time.sleep(1)
            print "connecting..."
            self.__connect(cb, topic, data)

    def send(self, topic, data):
        if self.producer is None:
            self.__connect(self.send, topic, data)
        else:
            try:
                serialized_data = serialize(Kafka_Message(data))
                self.producer.send(topic, serialized_data)
            except BaseException as e:
                print e
                self.producer.send(topic, data)
