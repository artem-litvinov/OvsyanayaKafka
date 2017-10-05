import re
import sys
import json
import pytest
from flask import url_for
sys.path.append('webserver')
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

@pytest.fixture
def accept_mimetype(mimetype):
    return [('Accept', mimetype)]

@pytest.fixture
def accept_multipart_form_data(request):
    return accept_mimetype('multipart/form-data')

@pytest.fixture
def accept_form_urlencoded(request):
    return accept_mimetype('application/x-www-form-urlencoded')

@pytest.fixture
def accept_json(request):
    return accept_mimetype('application/json')

@pytest.fixture(params=['*', '*/*'])
def accept_any(request):
    return accept_mimetype(request.param)

def test_root(client):
    assert True
#    assert client.get(url_for('*')).status_code == 200

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
    response = client.post('user', data = json.dumps(user), content_type='application/x-www-form-urlencoded')
    print response
#    assert re.compile('[0-9]+').match(response)

def test_post_send_message(client):
    user = {'uid': '123456', 'message': 'test'}
    response = client.post('send', data = json.dumps(user), content_type='application/x-www-form-urlencoded')
    print response
#    assert re.compile('[0-9]+').match(response)