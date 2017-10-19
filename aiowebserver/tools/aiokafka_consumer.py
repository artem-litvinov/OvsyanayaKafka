import os
import asyncio
from aiokafka import AIOKafkaConsumer
from thrift.TSerialization import serialize
from kafka_message.ttypes import KafkaMessage

loop = asyncio.get_event_loop()

class AIOConsumer(object):
    def __init__(self, loop, host='localhost', port='9092', topic='test-topic', group='test-group'):
        if loop is None:
            loop = asyncio.get_event_loop()
        self.__address = "%s:%s" % (host, port)
        self.__consumer = AIOKafkaConsumer(topic, loop=loop, bootstrap_servers=self.__address, group_id=group)

    async def consume(self):
        await self.__consumer.start()
        return self.__consumer

def create_consumer():
    try:
        KAFKA_HOST = os.environ['KAFKA_HOST']
    except KeyError as err:
        print(err, "Please set KAFKA_HOST environment variable")

    return AIOConsumer(loop, KAFKA_HOST, '9092')

async def main():
    consumer = create_consumer()
    m_stream = await consumer.consume()
    kafka_message = KafkaMessage()
    deserialize(kafka_message, msg.value)
    try:
        async for msg in m_stream:
            print("consumed: ", msg.topic, msg.partition, msg.offset, msg.key, msg.value, msg.timestamp)
            deserialize(kafka_message, msg.value)
            print(kafka_message)
    finally:
        await consumer.stop()


if __name__ == '__main__':
    print('entering test consumer')
    loop.run_until_complete(main())
    loop.close()