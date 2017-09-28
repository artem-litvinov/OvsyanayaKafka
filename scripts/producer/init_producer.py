import sys
import time
import random
from producer import AProducer


def run():
    mocks = [
        {
            'type': 'phone',
            'contact': '+79997305889',
            'message': 'test message from space to m0sk1t phone'
        },
        {
            'type': 'mail',
            'contact': 'm0sk1t@bk.ru',
            'message': 'test message from space to m0sk1t mail'
        },
        {
            'type': 'phone',
            'contact': '+79158334170',
            'message': 'test message from space to artlitvinov phone'
        },
        {
            'type': 'mail',
            'contact': 'work.litvinov.artem@gmail.com',
            'message': 'test message from space to artlitvinov mail'
        }
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
