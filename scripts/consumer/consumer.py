import sys
import json
import time
import boto3
import thread

from kafka import KafkaConsumer
sys.path.append('./thrift-gen')
from kafka_data.ttypes import Kafka_Data
from thrift.TSerialization import deserialize
from cassandra.cluster import Cluster

class AConsumer():
    def __init__(self, host='localhost', port='9092'):
        self.__host = host
        self.__port = port

    def __server(self):
        return self.__host + ':' + self.__port

    def __connect(self, cb, topic):
        try:
            self.consumer = KafkaConsumer(bootstrap_servers=self.__server())
            self.__client = boto3.client("sns")
            cluster = Cluster(['localhost']) #'35.162.115.250'
            self.session = cluster.connect('users')
            print "connected to host: ", self.__host, ", ", "port: ", self.__port
            cb(topic)
        except BaseException as e:
            print e
            time.sleep(1)
            print "connecting..."
            self.__connect(cb, topic)

    def listen(self, topic):
        if hasattr(self, 'consumer'):
            self.consumer.subscribe(topic)
            self.__topic_arn = self.__client.create_topic(Name=topic)['TopicArn']
            for msg in self.consumer:
                try:
                    self.__output(msg)
                    #thread.start_new_thread(self.__output, msg)
                except BaseException as e:
                    print e
                except:
                    print msg.value
        else:
            self.__connect(self.listen, topic)

    def __output(self, msg):
        data = Kafka_Data()
        deserialize(data, msg.value)
        self.session.execute('USE users')
        rows = self.session.execute("SELECT * FROM users WHERE user_id='%s'" % (data.contact))
        for row in rows:
            print row.contact
            print data.message
            # print self.__client.publish(
            #     TopicArn=self.__topic_arn,
            #     Message=data.message
            # )
