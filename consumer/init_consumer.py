import sys, os
#import boto3

from consumer import Consumer
from kafka_message.ttypes import KafkaMessage
from thrift.TSerialization import deserialize
from cassandra.cluster import Cluster

def callback(msg):
    kafka_message = KafkaMessage()
    deserialize(kafka_message, msg.value)
    print kafka_message
    
    #client = boto3.client("sns")
    cluster = Cluster(['172.17.0.2']) #'35.162.115.250'

    session = cluster.connect('users')
    m_rows = session.execute("SELECT * FROM messages WHERE mid='%s'" % (kafka_message.mid))

    for m_row in m_rows:
        print m_row

        u_rows = session.execute("SELECT * FROM users WHERE uid='%s'" % (m_row.uid))

        for u_row in u_rows:
            print u_row


            # print self.__client.publish(
            #     TopicArn=self.__topic_arn,
            #     Message=kafka_message.message
            # )
            session.execute("UPDATE messages SET status='sent' WHERE mid='%s'" % (m_row.mid))

def run():
    args = {'host': 'localhost', 'port': '9092'}
    for arg in sys.argv:
        entry = arg.split("=")
        if len(entry) == 2:
            args[str(entry[0])] = str(entry[1])
    consumer = Consumer(args['host'], args['port'])
    for msg in consumer.messages('test-topic'):
        callback(msg)

if __name__ == "__main__":
    run()
