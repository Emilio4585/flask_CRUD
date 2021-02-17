from flask import Flask, render_template, flash, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from models import User
from modulo import app,db



@app.route("/", methods=["POST", "GET"])
def home():

    all_data = User.query.all()

    
    return render_template("index.html", users = all_data)


@app.route('/new', methods=["POST", "GET"])
def create_user():
    

    if request.method == "POST":
        try:
            name = request.form.get("inputname")
            email= request.form.get("inputemail")
            address = request.form.get("inputAddress")
            phone = request.form.get("inputphone")

            user = User(name=name, email=email, address=address,phone=phone)

            user.add()

        except Exception as e:
            print("Fallo al añadir usuario")
            print(e)
  
  
    return redirect(url_for('home'))



@app.route("/update", methods=['POST','GET'])
def update_user():

    if request.method == "POST":

        try:

            iD = User.query.get(request.form.get("id"))
            iD.name = request.form.get("editname")
            iD.email= request.form.get("editemail")
            iD.address = request.form.get("editaddress")
            iD.phone = request.form.get("editphone")

            iD.update()
        
        except Exception as e:
            print("Fallo al actualizar el user")
            print(e)
    
    return redirect(url_for("home"))



if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)