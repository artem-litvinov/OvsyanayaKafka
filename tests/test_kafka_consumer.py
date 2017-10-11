import os
import mock
import pytest
from consumer.consumer import Consumer
from kafka.errors import NoBrokersAvailable


@pytest.fixture
@mock.patch.dict(os.environ, {'KAFKA_HOST':'localhost'})
def consumer():
    KAFKA_HOST = os.environ['KAFKA_HOST']
    consumer = Consumer(KAFKA_HOST, '9092')
    return consumer

@pytest.fixture
def fake_message_generator():
    class int_enumeration():
        def __init__(self, n):
            self.n = n
            self.num, self.nums = 1, []
        
        def __iter__(self):
            return self
        
        def __next__(self):
            return self.next()
    
        def next(self):
            if self.num <= self.n:
                cur, self.num = self.num, self.num+1
                return cur
            else:
                raise StopIteration()
    
    return int_enumeration(4)

def test_no_brokers_available_error():
    with pytest.raises(NoBrokersAvailable):
        c = Consumer('12.345.678.90', '9092')

def test_subscribe():
    c = consumer()
    c.subscribe('test-topic')

def test_fake_message_generator():
    c = consumer()
    c.consumer = fake_message_generator()
    messages = c.messages()
    assert sum(messages) == 10
    
