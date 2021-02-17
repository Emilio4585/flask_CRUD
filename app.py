from flask import Flask, render_template, flash, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from models import User
from modulo import app,db

@app.route("/", methods=["POST", "GET"])
def home():
    all_data = User.query.all()
    return render_template("index.html", users = all_data)

@app.route("/read/<int:pk>")
def read(pk):
    user = User.query.filter_by(id=pk).first()
    return redirect(url_for('home'))

@app.route('/new', methods=["POST", "GET"])
def create_user():
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email= request.form.get("email")
            address = request.form.get("address")
            phone = request.form.get("phone")
            user = User(name=name, email=email, address=address,phone=phone)
            user.add()
        except Exception as e:
            flash("there was a failure adding the user, try again")
            flash(e)
    return redirect(url_for('home'))

@app.route("/update/<int:pk>", methods=['POST','GET'])
def update_user(pk):
    if request.method == "POST":
        try:
            user = User.query.get(id=pk)
            user.name = request.form.get("name")
            user.email = request.form.get("email")
            user.address = request.form.get("address")
            user.phone = request.form.get("phone")
            user.update()
        except Exception as e:
            flash("update adding the user, try again")
            flash("there was a failure adding the user, try again")
    return redirect(url_for("home"))

@app.route("/delete/<int:pk>")
def delete(pk):
    user = User.query.filter_by(id=pk).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home'))

#delete y el read

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)