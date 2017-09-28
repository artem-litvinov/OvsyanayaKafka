import sys
sys.path.append('./thrift')
import json
import time

from kafka import KafkaProducer
from kafka_data.ttypes import Kafka_Data

from thrift.TSerialization import serialize
# from thrift.protocol import TBinaryProtocol
# from thrift.transport import TTransport

class AProducer():
    def __init__(self, host='localhost', port='9092'):
        self.__host = host
        self.__port = port

    def __server(self):
        return self.__host + ':' + self.__port

    def __connect(self, cb, topic, data):
        try:
            self.producer = KafkaProducer(bootstrap_servers=self.__server())
            print "connected to host: ", self.__host, ",", "port: ", self.__port
            cb(topic, data)
        except:
            time.sleep(1)
            print "connecting..."
            self.__connect(cb, topic, data)

    def send(self, topic, data):
        if hasattr(self, 'producer'):
            try:
                serialized_data = serialize(data)

                # transportOut = TTransport.TMemoryBuffer()
                # protocolOut = TBinaryProtocol.TBinaryProtocol(transportOut)
                # data.write(protocolOut)
                # bytes = transportOut.getvalue()

                self.producer.send(topic, serialized_data)
            except:
                self.producer.send(topic, data)
        else:
            self.__connect(self.send, topic, data)
