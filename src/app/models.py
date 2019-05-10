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