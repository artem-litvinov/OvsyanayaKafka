from producer import AProducer
a_producer = AProducer()
while True:
    data = raw_input('enter your data: ')
    a_producer.send('test-topic', data)
