import os
import time
import logging

from consumer import Consumer
from kafka_message.ttypes import KafkaMessage

import boto3
from thrift.TSerialization import deserialize
from cassandra.cluster import Cluster

if os.environ.has_key("DEBUG"):
    logging.basicConfig(level=logging.DEBUG)

def send_msg(client, contact, text):
    print client.publish(
        TopicArn="test-topic",
        Message=text
        )

def get_user_data(uid, session):
    user_rows = session.execute("SELECT * FROM users WHERE uid='%s'" % (uid))

    for user_row in user_rows:
        return user_row

def get_message_data(mid, session):
    msg_rows = session.execute("SELECT * FROM messages WHERE mid='%s'" % (mid))

    for msg_row in msg_rows:
        return msg_row

def deserialize_msg(msg):
    kafka_message = KafkaMessage()
    deserialize(kafka_message, msg.value)
    return kafka_message

def kafka_message_handler(session, sns_client, kafka_msg):
    kafka_msg = deserialize_msg(kafka_msg)
    logging.debug("Received message %s from Kafka", kafka_msg)

    msg = get_message_data(kafka_msg.mid, session)
    if msg is None:
        logging.warning(
            "Couldn't find message details for message %s", kafka_msg.mid)
        return

    user = get_user_data(msg.uid, session)
    if user is None:
        logging.warning(
            "Couldn't find user details for message %s", msg.uid)
        return

    print "send_msg(sns_client, %s, %s)" % (user.contact, msg.text)


if __name__ == "__main__":
    try:
        CASSANDRA_HOST = os.environ['CASSANDRA_HOST']
    except KeyError as err:
        print(err, "Please set CASSANDRA_HOST environment variable")
        raise

    try:
        KAFKA_HOST = os.environ['KAFKA_HOST']
    except KeyError as err:
        print(err, "Please set KAFKA_HOST environment variable")
        raise

    cluster = Cluster([CASSANDRA_HOST])
    session = cluster.connect('users')
    consumer = Consumer(KAFKA_HOST, '9092')
    sns_client = boto3.client("sns", region_name='us-west-2')

    for kafka_msg in consumer.messages('test-topic'):
        kafka_message_handler(session, sns_client, kafka_msg)

