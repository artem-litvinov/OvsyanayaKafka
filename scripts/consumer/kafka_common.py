"""
Kafka common
"""
class AKafkaCommon(object):
    def __init__(self, host = 'localhost', port = '9092'):
        self.__host = host
        self.__port = port

    def server(self):
        """
        Server instance string
        """
        return self.__host + ':' + self.__port
