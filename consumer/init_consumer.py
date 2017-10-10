import os
#import boto3

from consumer import Consumer
from kafka_message.ttypes import KafkaMessage
from thrift.TSerialization import deserialize
from cassandra.cluster import Cluster


KAFKA_HOST = os.environ['KAFKA_HOST']
CASSANDRA_HOST = os.environ['CASSANDRA_HOST']
def callback(msg):
    kafka_message = KafkaMessage()
    deserialize(kafka_message, msg.value)
    print kafka_message
    
    #client = boto3.client("sns")
    cluster = Cluster([CASSANDRA_HOST]) #'35.162.115.250'

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
    consumer = Consumer(KAFKA_HOST, '9092')
    for msg in consumer.messages('test-topic'):
        callback(msg)

if __name__ == "__main__":
    run()
