from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import users
from modulo import app,db



@app.route("/")
def home():

    return render_template("index.html")



if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)