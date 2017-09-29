import sys
import time
import random

from producer import AProducer
sys.path.append('./thrift-gen')
from kafka_data.ttypes import Kafka_Data

def run():
    mocks = [
#        Kafka_Data("sms", "+79997305889", "test message from space to m0sk1t phone"),
        Kafka_Data("email", "m0sk1t@bk.ru", "test message from space to m0sk1t mail"),
#        Kafka_Data("sms", "+79158334170", "test message from space to artlitvinov phone"),
        Kafka_Data("email", "work.litvinov.artem@gmail.com", "test message from space to artlitvinov mail")
    ]
    args = {'host': 'localhost', 'port': '9092'}
    for arg in sys.argv:
        entry = arg.split("=")
        if len(entry) == 2:
            args[str(entry[0])] = str(entry[1])
    a_producer = AProducer(args['host'], args['port'])
    while True:
        message = raw_input("Enter your message: ")
        mock = mocks[random.randint(0, 1)]
        mock.message = message
        a_producer.send('test-topic', mock)
        print "your message sent to", mock.contact

if __name__ == "__main__":
    run()
