#!/usr/bin/env python
from app import db

class Boroughs(db.Model):
    __tablename__ = "borough_lookup"
    borough_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Borough %s>' % self.name

    def json_dump(self):
        return dict(
            id=self.borough_id,
            name=self.name
        )

    @staticmethod
    def get_all():
        return [b.json_dump() for b in Boroughs.query.all()]

class Trips(db.Model):
    __tablename__ = "trip_summary"
    vendor_type = db.Column(db.String, primary_key=True)
    trip_date = db.Column(db.DateTime, primary_key=True)
    pickup_borough = db.Column(db.Integer, primary_key=True)
    dropoff_borough = db.Column(db.Integer, primary_key=True)
    number_of_trips = db.Column(db.Integer, nullable=False)
    elapsed_time_min = db.Column(db.Integer, nullable=False)
    total_distance = db.Column(db.Float, nullable=True)
    total_amount = db.Column(db.Float, nullable=True)
    total_tips = db.Column(db.Float, nullable=True)
    average_time = db.Column(db.Float, nullable=True)
    average_distance = db.Column(db.Float, nullable=True)
    average_amount = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return '<Trip %s-%s-%s-%s>' % (self.vendor_type, self.trip_date, self.pickup_borough, self.dropoff_borough)

    def json_dump(self):
        return dict(
            type=self.vendor_type,
            trip_date=self.trip_date,
            pickup_borough=self.pickup_borough,
            dropoff_borough=self.dropoff_borough,
            number_of_trips=self.number_of_trips,
            elapsed_time_min=self.elapsed_time_min,
            total_distance=self.total_distance,
            total_amount=self.total_amount,
            total_tips=self.total_tips,
            average_time=self.average_time,
            average_distance=self.average_distance,
            average_amount=self.average_amount
        )

    @staticmethod
    def get_all():
        return [t.json_dump() for t in Trips.query.all()]

    @staticmethod
    def get_all_filtered(from_borough=None, to_borough=None, car_type=None, args=None):
        query = Trips.query
        if from_borough is not None and to_borough is not None:
            query = query.filter(Trips.pickup_borough == from_borough).filter(Trips.dropoff_borough == to_borough)

        if car_type is not None:
            query = query.filter(Trips.vendor_type == car_type)

        if 'from' in args and 'to' in args:
            query = query.filter(Trips.trip_date >= args['from'])
            query = query.filter(Trips.trip_date <= args['to'])

        return [t.json_dump() for t in query.all()]