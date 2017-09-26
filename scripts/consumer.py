import json
from kafka import KafkaConsumer
from kafka_common import AKafkaCommon

class AConsumer(AKafkaCommon):
    """
    Kafka consumer
    """
    def __init__(self, host = 'localhost', port = '9092', *args, **kwargs):
        super(AConsumer, self).__init__(host, port, *args, **kwargs)
        self.consumer = KafkaConsumer(bootstrap_servers = self.server())

    """
    Listen data topic
    """
    def listen(self, topic):
        self.consumer.subscribe(topic)
        for msg in self.consumer:
            print json.loads(msg.value)
