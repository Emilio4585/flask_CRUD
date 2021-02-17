from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from modulo import db

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    