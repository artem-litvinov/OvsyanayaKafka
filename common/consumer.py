import sys
import json
import time
import thread

from kafka_common import AKafkaCommon
from kafka import KafkaConsumer

class AConsumer(AKafkaCommon):
    def __connect(self, topic, callback = None):
        try:
            self.consumer = KafkaConsumer(bootstrap_servers=self.server())
            self.listen(topic, callback)
        except BaseException as e:
            print e
            time.sleep(1)
            print "connecting..."
            self.__connect(topic, callback)

    def listen(self, topic, callback):
        if self.consumer is None:
            self.__connect(topic, callback)
        else:
            self.consumer.subscribe(topic)
            for msg in self.consumer:
                try:
                    callback(msg)
                    #thread.start_new_thread(self.__output, msg)
                except BaseException as e:
                    print e
