import os
import boto3
import asyncio
from aio_cassandra import create_cassandra
from aiokafka_consumer import create_consumer
from kafka_message.ttypes import KafkaMessage
from thrift.TSerialization import deserialize

loop = asyncio.get_event_loop()

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
    print(msg_rows)
    return msg_rows[0]

async def get_user_data(uid, session):
    user_rows = await session.get_from_table_by_id("users", str(uid))
    print(user_rows)
    return user_rows[0]

async def kafka_message_handler(session, sns_client, kafka_msg):
    kafka_msg = deserialize_msg(kafka_msg)
    msg = await get_message_data(kafka_msg.id, session)
    user = await get_user_data(msg.uid, session)
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
        
