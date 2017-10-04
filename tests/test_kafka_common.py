import os, sys
import unittest
sys.path.append('../common')
from kafka_common import AKafkaCommon

class TestStringMethods(unittest.TestCase):

    def test_empty(self):
        kafka = AKafkaCommon()
        self.assertEqual(kafka.server(), 'localhost:9092')

    def test_aws_ip(self):
        kafka = AKafkaCommon('34.214.200.68')
        self.assertEqual(kafka.server(), '34.214.200.68:9092')

    def test_aws_ip_port(self):
        kafka = AKafkaCommon('34.214.200.68', '9156')
        self.assertEqual(kafka.server(), '34.214.200.68:9156')


if __name__ == '__main__':
    unittest.main()