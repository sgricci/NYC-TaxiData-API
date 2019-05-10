import os
import tempfile

import pytest

from app import app
from flask import g
import sqlite3

@pytest.fixture
def client():
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['DATABASE'] = 'sqlite:///'+os.path.join(basedir, 'data/test.db')
    app.config['TESTING'] = True

    client = app.test_client()

    yield client

def test_working(client):

    rv = client.get('/')
    assert 'version' in rv.json
    
def test_404(client):

    rv = client.get('/this-url-never-exists')
    assert 'status' in rv.json
    assert 404 == rv.json['status']