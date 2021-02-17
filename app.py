from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import users
from modulo import app,db



@app.route("/", methods=["POST", "GET"])
def home():

    all_data = users.query.all()

    

    return render_template("index.html", users = all_data)



if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)