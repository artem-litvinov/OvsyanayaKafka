import sys
sys.path.append('./thrift')
import json
import time

from kafka import KafkaConsumer
from kafka_data.ttypes import Kafka_Data

from thrift.TSerialization import deserialize

class AConsumer():
    def __init__(self, host='localhost', port='9092'):
        self.__host = host
        self.__port = port

    def __server(self):
        return self.__host + ':' + self.__port

    def __connect(self, cb, topic):
        try:
            self.consumer = KafkaConsumer(bootstrap_servers=self.__server())
            print "connected to host: ", self.__host, ", ", "port: ", self.__port
            cb(topic)
        except:
            time.sleep(1)
            print "connecting..."
            self.__connect(cb, topic)

    def listen(self, topic):
        if hasattr(self, 'consumer'):
            self.consumer.subscribe(topic)
            for msg in self.consumer:
                try:
                    data = Kafka_Data()
                    deserialize(data, msg.value)
                    
                    print data
                except:
                    print msg.value
        else:
            self.__connect(self.listen, topic)
