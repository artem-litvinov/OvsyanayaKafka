import sys
import pytest
from flask import url_for
sys.path.append('webserver')
from app import create_app


@pytest.fixture
def app():
    app = create_app()
    return app