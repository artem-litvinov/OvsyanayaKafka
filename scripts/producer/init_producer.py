from producer import AProducer

def run():
    a_producer = AProducer()
    while True:
        try:
            data = raw_input('enter your data: ')
            a_producer.send('test-topic', data)
        except EOFError:
            pass

run()