import sys
import json
import time
import thread

from kafka_common import AKafkaCommon
from kafka import KafkaConsumer

class AConsumer(AKafkaCommon):
    def __connect(self, cb, topic):
        try:
            self.consumer = KafkaConsumer(bootstrap_servers=self.server())

            print "connected to host: ", self.__host, ", ", "port: ", self.__port
            cb(topic)
        except BaseException as e:
            print e
            time.sleep(1)
            print "connecting..."
            self.__connect(cb, topic)

    def listen(self, topic, callback):
        if hasattr(self, 'consumer'):
            self.consumer.subscribe(topic)

            for msg in self.consumer:
                try:
                    callback(msg)
                    #thread.start_new_thread(self.__output, msg)
                except BaseException as e:
                    print e
                except:
                    print msg.value
        else:
            self.__connect(self.listen, topic)

