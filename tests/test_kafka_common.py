import os, sys
import pytest
sys.path.append('common')
from kafka_common import AKafkaCommon

def test_empty():
    kafka = AKafkaCommon()
    assert(kafka.server() == 'localhost:9092')

def test_aws_ip():
    kafka = AKafkaCommon('34.214.200.68')
    assert(kafka.server() == '34.214.200.68:9092')

def test_aws_host_is_none_typeerror():
    with pytest.raises(TypeError):
        kafka = AKafkaCommon(None, '9156')
        assert(kafka.server() == '34.214.200.68:9092')

def test_aws_ip_port():
    kafka = AKafkaCommon('34.214.200.68', '9156')
    assert(kafka.server() == '34.214.200.68:9156')

def test_list_param_typeerror():
    with pytest.raises(TypeError):
        kafka = AKafkaCommon(('34.214.200.68', '9156'))
        assert(kafka.server() == '34.214.200.68:9156')
