import json
from kafka import KafkaProducer
from kafka_common import AKafkaCommon

class AProducer(AKafkaCommon):
    """
    Kafka producer
    """
    def __init__(self, host = '0.0.0.0', port = '9092', *args, **kwargs):
        super(AProducer, self).__init__(host, port, *args, **kwargs)
        self.producer = KafkaProducer(bootstrap_servers = self.server())

    def send(self, topic, data):
        """
        Sends data to topic
        """
        try:
            data = json.dumps(data)
            self.producer.send(topic, json.dumps(data))
        except:
            self.producer.send(topic, data)
