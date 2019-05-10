#!/usr/bin/env python

from app import app, models
from flask import jsonify

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