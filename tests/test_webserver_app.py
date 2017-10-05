import re
import sys
import json
import pytest
from flask import url_for
sys.path.append('webserver')
from app import create_app

digit_only_pattern = re.compile('[0-9]+')

@pytest.fixture
def app():
    app = create_app()
    return app

def test_root(client):
    assert client.get(url_for('/')).status_code == 200

def test_index(client):
    assert client.get(url_for('/index')).status_code == 200

def test_sender(client):
    assert client.get(url_for('/sender')).status_code == 200

def test_users(client):
    assert len(client.get(url_for('/user/all')).json) == 2

def test_user(client):
    user = client.get(url_for('/user/all')).json[0]
    assert client.get(url_for('/user/$s'%(user.uid))).json["uid"] == user.uid

def test_post_create_user(client):
    user = {'name': 'User Name', 'contact': 'user@name.com'}
    assert digit_only_pattern.match(client.post('/user', data = json.dumps(user), content_type='application/json'))

def test_post_send_message(client):
    user = {'uid': '123456', 'message': 'test'}
    digit_only_pattern.match(client.post('/send', data = json.dumps(user), content_type='application/json'))