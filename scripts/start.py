from consumer import AConsumer
from producer import AProducer

a_producer = AProducer()
a_consumer = AConsumer()

a_consumer.listen('test-topic')

a_producer.send('test-topic', 'test data 1')
a_producer.send('test-topic', 'test data 2')
a_producer.send('test-topic', 'test data 3')
