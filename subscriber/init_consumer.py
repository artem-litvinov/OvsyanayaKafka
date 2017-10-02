import sys
import boto3

from consumer import AConsumer
sys.path.append('./gen-py')
from kafka_message.ttypes import Kafka_Message
from thrift.TSerialization import deserialize
from cassandra.cluster import Cluster

def callback(msg):
    kafka_message = Kafka_Message()
    deserialize(kafka_message, msg.value)

    client = boto3.client("sns")
    cluster = Cluster(['localhost']) #'35.162.115.250'

    session = cluster.connect('messages')
    m_rows = session.execute("SELECT * FROM messages WHERE mid='%s'" % (kafka_message.mid))

    for m_row in m_rows:
        print m_row

        session.execute('USE users')
        u_rows = session.execute("SELECT * FROM users WHERE uid='%s'" % (m_row.uid))

        for u_row in u_rows:
            print u_row

            # topic_arn = client.create_topic(Name=topic)['TopicArn']

            # print self.__client.publish(
            #     TopicArn=self.__topic_arn,
            #     Message=kafka_message.message
            # )

def run():
    args = {'host': 'localhost', 'port': '9092'}
    for arg in sys.argv:
        entry = arg.split("=")
        if len(entry) == 2:
            args[str(entry[0])] = str(entry[1])
    a_consumer = AConsumer(args['host'], args['port'])
    a_consumer.listen('test-topic', callback)

if __name__ == "__main__":
    run()
