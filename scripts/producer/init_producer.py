import sys
from producer import AProducer

def run():
    args = {'host': 'localhost', 'port': '9092'}
    for arg in sys.argv:
        entry = arg.split("=")
        if len(entry) == 2:
            args[str(entry[0])] = str(entry[1])
    a_producer = AProducer(args['host'], args['port'])
    while True:
        try:
            data = raw_input('enter your data: ')
            a_producer.send('test-topic', data)
        except EOFError:
            pass

if __name__ == "__main__":
    run()