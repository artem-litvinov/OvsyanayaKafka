import os
import time
import logging

import boto3
import asyncio
from consumer import Consumer
from aio_cassandra import create_cassandra
from aiokafka_consumer import create_consumer
from kafka_message.ttypes import KafkaMessage
from thrift.TSerialization import deserialize

loop = asyncio.get_event_loop()

if os.environ.has_key("DEBUG"):
    logging.basicConfig(level=logging.DEBUG)

def send_msg(client, contact, text):
    print (client.publish(
        TopicArn="test-topic", 
        Message=text
        ))

def deserialize_msg(msg):
    kafka_message = KafkaMessage()
    deserialize(kafka_message, msg.value)
    return kafka_message

async def get_message_data(mid, session):
    msg_rows = await session.get_from_table_by_id("messages", str(mid))
    if len(msg_rows) > 0:
        return msg_rows[0]
    return None

async def get_user_data(uid, session):
    user_rows = await session.get_from_table_by_id("users", str(uid))
    if len(user_rows) > 0:
        return user_rows[0]
    return None

async def kafka_message_handler(session, sns_client, kafka_msg):
    kafka_msg = deserialize_msg(kafka_msg)
    msg = await get_message_data(kafka_msg.id, session)
    if msg is None:
        logging.warning(
            "Couldn't find message details for message %s", kafka_msg.mid)
        return

    user = await get_user_data(msg.uid, session)
    if user is None:
        logging.warning(
            "Couldn't find user details for message %s", msg.uid)
        return

    print("send_msg(sns_client, %s, %s)" % (user.contact, msg.text))

async def main():
    sns_client = boto3.client("sns", region_name='us-west-2')
    cassandra = create_cassandra()
    cassandra.connect(loop, keyspace='users')

    consumer = create_consumer('test-topic', 'test')
    kafka_stream = await consumer.consume()
    try:
        async for kafka_msg in kafka_stream:
            print(kafka_msg)
            await kafka_message_handler(cassandra, sns_client, kafka_msg)
    finally:
        await consumer.stop()

if __name__ == "__main__":
    loop.run_until_complete(main())
    loop.close()
        
