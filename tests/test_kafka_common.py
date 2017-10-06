import sys
import pytest
sys.path.append('common')
from kafka_common import AKafkaCommon

def test_empty():
    kafka = AKafkaCommon()
    assert(kafka.server() == 'localhost:9092')

def test_server_ip():
    kafka = AKafkaCommon('server_ip_with_standard_port')
    assert(kafka.server() == 'server_ip_with_standard_port:9092')

def test_server_ip_port():
    kafka = AKafkaCommon('server_ip', 'server_port')
    assert(kafka.server() == 'server_ip:server_port')

def test_different_server_ip():
    kafka = AKafkaCommon('fake_server_ip', 'server_port')
    assert(kafka.server() != 'server_ip:server_port')

def test_server_host_is_none_typeerror():
    with pytest.raises(TypeError):
        kafka = AKafkaCommon(None, '9092')
        assert(kafka.server() == 'server_ip_with_standard_port:9092')

def test_list_param_typeerror():
    with pytest.raises(TypeError):
        kafka = AKafkaCommon(('wrong_arguments', 'list_param'))
        assert(kafka.server() == 'server_ip:server_port')
