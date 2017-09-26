import json
from kafka import KafkaProducer
from kafka_common import AKafkaCommon

class AProducer(AKafkaCommon):
    """
    Kafka producer
    """
    def __init__(self, host = 'localhost', port = '9092', *args, **kwargs):
        super(AProducer, self).__init__(host, port, *args, **kwargs)
        self.producer = KafkaProducer(bootstrap_servers = self.server())

    """
    Sends data to topic
    """
    def send(self, topic, data):
        data = json.dumps(data)
        self.producer.send(topic, data)
