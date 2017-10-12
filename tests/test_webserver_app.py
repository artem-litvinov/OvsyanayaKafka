import os
import re
import mock
import json
import pytest
from flask import url_for
from pytest_flask.fixtures import client
from webserver.app import create_app

class UserRow():
    def __init__(self, 
                    uid = '1',
                    name = 'test.name',
                    u_type = 'test.type',
                    contact = 'test.contact',
                ):
        self.uid = uid
        self.name = name
        self.type = u_type
        self.contact = contact

class MsgRow():
    def __init__(self,
                    mid = '1',
                    date = 'test.date',
                    status = 'test.status',
                    text = 'test.test',
                    uid = '1'
                ):
        self.mid = mid
        self.date = date
        self.status = status
        self.text = text
        self.uid = uid

class Session():
    def execute(self, request, *args, **kvargs):
        if "users" in request:
            return [UserRow(), UserRow(), UserRow()]

        if "messages" in request:
            return [MsgRow('1'), MsgRow('2'), MsgRow('3')]

class CassandraCluster():
    def connect(self, *args, **kvargs):
        return Session()

class Producer():
    def send(self, *args, **kvargs):
        print(args, kvargs)

@pytest.fixture
def cluster():
    return CassandraCluster()

@pytest.fixture
def producer():
    return Producer()

@pytest.fixture
@mock.patch.dict(os.environ, {'WEBSERVER_PORT':'5000'})
@mock.patch.dict(os.environ, {'KAFKA_HOST':'localhost'})
@mock.patch.dict(os.environ, {'CASSANDRA_HOST':'localhost'})
def app(cluster, producer):
    return create_app(cluster.connect(), producer)

def test_index(client):
    assert client.get(url_for('index')).status_code == 200

def test_sender(client):
    assert client.get(url_for('sender')).status_code == 200

def test_users(client):
    users = client.get(url_for('user', id='all')).json
    assert len(users) >= 2

def test_user(client):
    user = client.get(url_for('user', id='all')).json[0]
    user_by_id = client.get(url_for('user', id=user["uid"])).json
    assert re.compile('[0-9]+').match(user_by_id["uid"])

def test_post_create_user(client):
    user = {'name': 'User Name', 'type': 'email','contact': 'user@name.com'}
    response = client.post('user', data = json.dumps(user), content_type='application/json')
    assert re.compile('[0-9]+').match(str(response.json))
    assert response.status_code == 200

def test_post_send_message(client):
    message = {'uid': '123456', 'message': 'test'}
    response = client.post('send', data = json.dumps(message), content_type='application/json')
    assert re.compile('[0-9]+').match(str(response.json))
    assert response.status_code == 200
