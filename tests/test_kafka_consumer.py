''' import boto3
import pytest

from kafka.errors import NoBrokersAvailable
from thrift.TSerialization import serialize
from tests.test_webserver_app import cluster
from consumer.kafka_message.ttypes import KafkaMessage
from consumer.init_consumer import kafka_message_handler

class KafkaMessageEnumeration():
    def __init__(self, count):
        self.count = count
        self.num = 1
    
    def __iter__(self):
        return self

    def next(self):
        if self.num <= self.count:
            cur, self.num = str(self.num), self.num+1
            msg = KafkaMessage(cur)
            s_msg = serialize(msg)
            return DictionaryMock(value=s_msg)
        else:
            raise StopIteration()

class DictionaryMock(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class FakeConsumer():
    def messages(self, *args, **kvargs):
        return KafkaMessageEnumeration(3)

@pytest.fixture
def fake_consumer():
    return FakeConsumer()

def test_no_brokers_available_error():
    with pytest.raises(NoBrokersAvailable):
        c = Consumer('12.345.678.90', '9092')

def test_kafka_message_handler():
    session = cluster().connect('users')
    consumer = FakeConsumer()
    sns_client = boto3.client("sns", region_name='us-west-2')

    for kafka_msg in consumer.messages('test-topic'):
        kafka_message_handler(session, sns_client, kafka_msg)
 '''