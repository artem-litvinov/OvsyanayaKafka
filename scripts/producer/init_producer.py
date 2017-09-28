import sys
import time
import random

from producer import AProducer
sys.path.append('./thrift')
from kafka_data.ttypes import Kafka_Data

def run():
    mocks = [
        Kafka_Data("phone", "+79997305889", "test message from space to m0sk1t phone"),
        Kafka_Data("mail", "m0sk1t@bk.ru", "test message from space to m0sk1t mail"),
        Kafka_Data("phone", "+79158334170", "test message from space to artlitvinov phone"),
        Kafka_Data("mail", "work.litvinov.artem@gmail.com", "test message from space to artlitvinov mail")
    ]
    args = {'host': 'localhost', 'port': '9092'}
    for arg in sys.argv:
        entry = arg.split("=")
        if len(entry) == 2:
            args[str(entry[0])] = str(entry[1])
    a_producer = AProducer(args['host'], args['port'])
    '''
        for message in mocks:
            time.sleep(1)
            a_producer.send('test-topic', message)
    '''
    while True:
        time.sleep(1)
        a_producer.send('test-topic', mocks[random.randint(0, 3)])



if __name__ == "__main__":
    run()
