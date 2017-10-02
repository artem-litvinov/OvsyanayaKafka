import sys
import json
import time

from kafka_common import AKafkaCommon
from kafka import KafkaProducer
sys.path.append('./gen-py')
from kafka_data.ttypes import Kafka_Data
from thrift.TSerialization import serialize
from cassandra.cluster import Cluster


class AProducer(AKafkaCommon):
    def __connect(self, cb, topic, data):
        try:
            self.producer = KafkaProducer(bootstrap_servers=self.server())
            cluster = Cluster(['localhost']) #'35.162.115.250'
            self.session = cluster.connect('users')
            print "connected to host: ", self.__host, ",", "port: ", self.__port
            cb(topic, data)
        except BaseException as e:
            print e
            time.sleep(1)
            print "connecting..."
            self.__connect(cb, topic, data)

    def send(self, topic, data):
        if hasattr(self, 'producer'):
            try:
                self.session.execute('USE users')
                user_id = str(int(round(time.time() * 1000)))
                print self.session.execute("INSERT INTO users (user_id, type, contact) VALUES (%s, %s, %s)", (user_id, data.type, data.contact))
                serialized_data = serialize(Kafka_Data(data.type, user_id, data.message ))
                self.producer.send(topic, serialized_data)
            except BaseException as e:
                print e
                self.producer.send(topic, data)
        else:
            self.__connect(self.send, topic, data)
