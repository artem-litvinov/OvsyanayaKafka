import json
import time
from kafka import KafkaProducer
from kafka_common import AKafkaCommon

class AProducer(AKafkaCommon):
    """
    Kafka producer
    """
    def __init__(self, host = 'localhost', port = '9092', *args, **kwargs):
        super(AProducer, self).__init__(host, port, *args, **kwargs)

    def __connect(self, cb, topic, data):
        try:
            self.producer = KafkaProducer(bootstrap_servers = self.server())
            cb(topic, data)
        except:
            time.sleep(1000)
            self.__connect(cb, topic, data)

    def send(self, topic, data):
        """
        Sends data to topic
        """
        if hasattr(self, 'producer'):
            try:
                data = json.dumps(data)
                self.producer.send(topic, json.dumps(data))
            except:
                self.producer.send(topic, data)
        else:
            self.__connect(self.send, topic, data)
