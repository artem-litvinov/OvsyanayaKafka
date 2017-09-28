import sys
from consumer import AConsumer


def run():
    args = {'host': 'localhost', 'port': '9092'}
    for arg in sys.argv:
        entry = arg.split("=")
        if len(entry) == 2:
            args[str(entry[0])] = str(entry[1])
    a_consumer = AConsumer(args['host'], args['port'])
    a_consumer.listen('test-topic')


if __name__ == "__main__":
    run()
