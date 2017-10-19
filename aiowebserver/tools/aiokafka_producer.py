import os
import time
import asyncio
from aiokafka import AIOKafkaProducer
from thrift.TSerialization import serialize
from kafka_message.ttypes import KafkaMessage

loop = asyncio.get_event_loop()

class AIOProducer(object):
    def __init__(self, loop, host='localhost', port='9092'):
        if loop is None:
            loop = asyncio.get_event_loop()
        self.__address = "%s:%s" % (host, port)
        self.__producer = AIOKafkaProducer(loop=loop, bootstrap_servers=self.__address)

    async def send(self, topic, data):
        serialized_data = serialize(KafkaMessage(data))
        await self.__producer.start()
        try:
            await self.__producer.send_and_wait(topic, serialized_data)
        finally:
            await self.__producer.stop()

def create_producer():
    try:
        KAFKA_HOST = os.environ['KAFKA_HOST']
    except KeyError as err:
        print(err, "Please set KAFKA_HOST environment variable")
    return AIOProducer(loop, KAFKA_HOST, '9092')

async def main():
    producer = create_producer()
    await producer.send('test-topic', '1507300909746')


if __name__ == "__main__":
    print('entering test producer')
    loop.run_until_complete(main())
    loop.close()
