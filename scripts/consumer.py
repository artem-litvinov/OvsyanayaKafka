import json
from kafka import KafkaConsumer
from kafka_common import AKafkaCommon

class AConsumer(AKafkaCommon):
    """
    Kafka consumer
    """
    def __init__(self, host = '0.0.0.0', port = '9092', *args, **kwargs):
        super(AConsumer, self).__init__(host, port, *args, **kwargs)
        self.consumer = KafkaConsumer(bootstrap_servers = self.server())

    def listen(self, topic):
        """
        Listen data topic
        """
        self.consumer.subscribe(topic)
        for msg in self.consumer:
            try:
                print json.loads(msg.value)
            except:
                print msg.value
