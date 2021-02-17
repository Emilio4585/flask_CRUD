from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from modulo import db

class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True, )
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    address = db.Column(db.String(200))
    phone = db.Column(db.Integer)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
        

    def __repr__(self):
        return "<Name: {}>".format(self.name)