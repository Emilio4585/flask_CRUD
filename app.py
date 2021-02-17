from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from models import User
from modulo import app,db



@app.route("/")
def home():
    return render_template("index.html")

@app.route('/new')
def create_user():
    users = None
    if request.form:
        try:
            id = request.form.get("id")
            name = request.form.get("name")
            email= request.form.get("email")
            address = request.form.get("adress")
            phone = request.form.get("phone")
            user = User(id=id, name=name, email=email, address=address,phone=phone)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print("Fallo al añadir usuario")
            print(e)
    users = User.query.all()
    return render_template("index.html", users=users)

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)