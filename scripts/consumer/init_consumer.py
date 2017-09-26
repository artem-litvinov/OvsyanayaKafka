from consumer import AConsumer

def run():
    a_consumer = AConsumer()
    a_consumer.listen('test-topic')

run()