from django.db import models


class Site(models.Model):
    name = db.Column(db.String(100), unique=True)
    site_code = db.Column(db.String(10), unique=True)
    region = db.Column(db.String(100))
    environ = db.Column('environment', db.String(100))
    url = db.Column(db.String(250))
    map_url = db.Column(db.String(250))
    lat = db.Column('latitude', db.String(50))
    long = db.Column('longitude', db.String(50))
    data = db.relationship('Data', backref='owner', lazy='dynamic')
    current = db.relationship('Current', backref='site', lazy='dynamic')


class Data(models.Model):
    site_id = db.Column(db.Integer, db.ForeignKey('sites.id'), nullable=False)
    o3 = db.Column(db.String(10), nullable=False)
    no2 = db.Column(db.String(10), nullable=False)
    so2 = db.Column(db.String(10), nullable=False)
    pm25 = db.Column(db.String(10), nullable=False)
    pm10 = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(50), nullable=False)