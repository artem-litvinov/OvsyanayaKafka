import json
import time
import boto3

from kafka import KafkaConsumer


class AConsumer():
    def __init__(self, host='localhost', port='9092'):
        self.__host = host
        self.__port = port

    def __server(self):
        return self.__host + ':' + self.__port

    def __connect(self, cb, topic):
        try:
            self.consumer = KafkaConsumer(bootstrap_servers=self.__server())
            self.client = boto3.client(
                "sns",
                aws_access_key_id="AKIAI7ANTPLUGZATSHOQ",
                aws_secret_access_key="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",
                region_name="us-west-2"
            )
            print "connected to host: ", self.__host, ", ", "port: ", self.__port
            cb(topic)
        except BaseException as e:
            print e
            time.sleep(1)
            print "connecting..."
            self.__connect(cb, topic)

    def listen(self, topic):
        if hasattr(self, 'consumer'):
            self.consumer.subscribe(topic)
            topic_arn = self.client.create_topic(Name=topic)['TopicArn']
            for msg in self.consumer:
                try:
                    message = json.loads(msg.value)
                    print message
                    self.client.subscribe(
                        TopicArn=topic_arn,
                        Protocol=message["proto"],
                        Endpoint=message["contact"]
                    )
                    print self.client.publish(
                        TopicArn=topic_arn,
                        Message=message["message"]
                    )
                except BaseException as e:
                    print e
                    print msg.value
        else:
            self.__connect(self.listen, topic)
