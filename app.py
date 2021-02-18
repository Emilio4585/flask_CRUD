from flask import Flask, render_template, flash, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from models import User
from modulo import app,db

@app.route("/", methods=["POST", "GET"])

def home():
    users_per_page = 5
    all_data = User.query.all()
    total_user = len(User.query.all())
    page = request.args.get('page',1, type =int)
    
    users = User.query.paginate(page=page, per_page = users_per_page)

    return render_template("index.html",User = users)

@app.route('/new', methods=["POST", "GET"])
def new_user():
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email= request.form.get("email")
            address = request.form.get("address")
            phone = request.form.get("phone")
            user = User(name=name, email=email, address=address,phone=phone)
            user.add()
        except Exception as e:
            flash("There was a failure adding the user try again")
            print("Fallo al añadir usuario")
            print(e)
    return redirect(url_for('home'))

@app.route("/update/<int:pk>", methods=['POST','GET'])
def update_user(pk):
    if request.method == "POST":
        try:
            user = User.query.filter_by(_id=pk).first()
            user.name = request.form.get("name")
            user.email = request.form.get("email")
            user.address = request.form.get("address")
            user.phone = request.form.get("phone")
            user.update()
            
        except Exception as e:
            flash("There was a failure to update the user try again")
            print("Fallo al actualizar el user")
            print(e)
    return redirect(url_for("home"))

@app.route("/delete/<int:pk>")
def delete_user(pk):
    user = User.query.filter_by(_id=pk).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home'))

#delete y el read

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)