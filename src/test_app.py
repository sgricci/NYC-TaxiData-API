import os
import tempfile
import datetime

import pytest

from app import app, models, db
from flask import g
import sqlite3

@pytest.fixture
def client():
    basedir = os.path.abspath(os.path.dirname(__file__))
    #app.config['DATABASE'] = 'sqlite:///'+os.path.join(basedir, 'data/test.db')
    app.config['TESTING'] = True

    client = app.test_client()
    with app.app_context():
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()


def test_working(client):

    rv = client.get('/')
    assert 'version' in rv.json
    
def test_404(client):

    rv = client.get('/this-url-never-exists')
    assert 'status' in rv.json
    assert 404 == rv.json['status']

def test_boroughs(client):
    borough = models.Boroughs(borough_id=1, name="Test")
    db.session.add(borough)

    boroughs = models.Boroughs.get_all()
    assert boroughs is not None
    assert len(boroughs) == 1

def test_boroughs_endpoint_empty(client):
    rv = client.get('/boroughs')

    assert 'status' in rv.json
    assert 'data' in rv.json
    assert 'length' in rv.json

    assert rv.json['length'] == 0

def test_boroughs_endpoint_with_data(client):
    borough = models.Boroughs(borough_id=1, name="Test")
    db.session.add(borough)
    borough = models.Boroughs(borough_id=2, name="Another Test")
    db.session.add(borough)

    rv = client.get('/boroughs')

    assert 'status' in rv.json
    assert 'data' in rv.json
    assert 'length' in rv.json

    assert rv.json['status'] != 404
    assert rv.json['length'] == 2

def test_trips_endpoint_empty(client):
    rv = client.get('/trips')

    assert 'status' in rv.json
    assert 'data' in rv.json
    assert 'length' in rv.json

    assert rv.json['length'] == 0

def create_test_trips():
    trip = models.Trips(
        vendor_type="green", 
        trip_date=datetime.datetime(2018,1,10,10,0,0),
        pickup_borough=1,
        dropoff_borough=4,
        number_of_trips=5,
        elapsed_time_min=5,
        total_distance=5,
        total_amount=5,
        total_tips=5,
        average_time=5,
        average_distance=5,
        average_amount=5
    )
    db.session.add(trip)
    trip = models.Trips(
        vendor_type="fhv", 
        trip_date=datetime.datetime(2018,1,5,20,0,0),
        pickup_borough=4,
        dropoff_borough=1,
        number_of_trips=5,
        elapsed_time_min=5,
        total_distance=5,
        total_amount=5,
        total_tips=5,
        average_time=5,
        average_distance=5,
        average_amount=5
    )
    db.session.add(trip)

def test_trips_endpoint_with_data(client):
    create_test_trips()

    rv = client.get('/trips')

    assert 'status' in rv.json
    assert 'data' in rv.json
    assert 'length' in rv.json

    assert rv.json['status'] != 404
    assert rv.json['length'] == 2

def test_trips_endpoint_filter_by_borough(client):
    create_test_trips()

    rv = client.get('/trips/4/1')

    assert 'status' in rv.json
    assert 'data' in rv.json
    assert 'length' in rv.json

    assert rv.json['status'] != 404
    assert rv.json['length'] == 1

def test_trips_endpoint_filter_by_date(client):
    create_test_trips()

    rv = client.get('/trips?from=2018-01-01&to=2018-01-06')

    assert 'status' in rv.json
    assert 'data' in rv.json
    assert 'length' in rv.json

    assert rv.json['status'] != 404
    assert rv.json['length'] == 1

def test_trips_endpoint_filter_by_date_and_borough(client):
    create_test_trips()

    rv = client.get('/trips/4/1?from=2018-01-01&to=2018-01-06')

    assert 'status' in rv.json
    assert 'data' in rv.json
    assert 'length' in rv.json

    assert rv.json['status'] != 404
    assert rv.json['length'] == 1

def test_trips_endpoint_filter_by_date_type_and_borough(client):
    create_test_trips()

    rv = client.get('/trips/4/1/fhv?from=2018-01-01&to=2018-01-06')

    assert 'status' in rv.json
    assert 'data' in rv.json
    assert 'length' in rv.json

    assert rv.json['status'] != 404
    assert rv.json['length'] == 1

def test_trips_endpoint_filter_by_type(client):
    create_test_trips()

    rv = client.get('/trips/green?from=2018-01-01&to=2018-01-06')

    assert 'status' in rv.json
    assert 'data' in rv.json
    assert 'length' in rv.json

    assert rv.json['status'] != 404
    assert rv.json['length'] == 0

def test_trips_endpoint_filter_by_type_alt(client):
    create_test_trips()

    rv = client.get('/trips/fhv?from=2018-01-01&to=2018-01-06')

    assert 'status' in rv.json
    assert 'data' in rv.json
    assert 'length' in rv.json

    assert rv.json['status'] != 404
    assert rv.json['length'] == 1
