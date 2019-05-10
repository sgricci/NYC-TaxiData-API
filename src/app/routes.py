#!/usr/bin/env python

from app import app, models
from flask import jsonify, request

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'status': 404, 'length': 0, 'data':str(e)})

@app.route('/')
def index():
    return jsonify(
        {
            'version': '1.0',
            'author': 'sgricci',
            'license': 'MIT',
            'href': 'https://github.com/sgricci/NYC-TaxiData-API',
            'contact': 'steve@gricci.org'
        }
    )

@app.route('/boroughs')
def boroughs():
    data = models.Boroughs.get_all()
    return resp_ok(data)

@app.route('/trips')
def trips():
    args = request.args.to_dict()
    return filtered_trips(None, None, None, args)

@app.route('/trips/<car_type>')
def trips_type(car_type):
    args = request.args.to_dict()
    return filtered_trips(None, None, car_type, args)

@app.route('/trips/<int:from_borough>/<int:to_borough>')
def trips_boroughs(from_borough, to_borough):
    print(from_borough)
    print(to_borough)
    args = request.args.to_dict()
    return filtered_trips(from_borough, to_borough, None, args)

@app.route('/trips/<int:from_borough>/<int:to_borough>/<car_type>')
def trips_all(from_borough, to_borough, car_type):
    args = request.args.to_dict()
    return filtered_trips(from_borough, to_borough, car_type, args)

def filtered_trips(from_borough=None, to_borough=None, car_type=None, args=None):
    data = models.Trips.get_all_filtered(from_borough, to_borough, car_type, args)
    return resp_ok(data)



def resp_ok(data):
    return jsonify({
        'data':data, 
        'status':200,
        'length':len(data)
        })

def resp_nodata():
    return jsonify({
        'data': {},
        'status': 200,
        'length': 0
        })