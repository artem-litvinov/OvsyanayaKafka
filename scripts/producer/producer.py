import json
import time
from kafka import KafkaProducer


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
            time.sleep(1000)
            print "connecting..."
            self.__connect(cb, topic, data)

    def send(self, topic, data):
        if hasattr(self, 'producer'):
            try:
                self.producer.send(topic, json.dumps(data))
            except:
                self.producer.send(topic, data)
        else:
            self.__connect(self.send, topic, data)
