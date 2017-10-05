import sys
import pytest
from flask import url_for
sys.path.append('webserver')
from app import create_app


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
    assert len(client.get(url_for('/user/all')).status_code) == 2

def test_user(client):
    user = client.get(url_for('/user/all')).json[0]
    assert client.get(url_for('/user/$s'%(user.uid))).json["uid"] == user.uid
