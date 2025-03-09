#Authentication routes
#This file contains the routes for login, sign-up and logout

from flask import Blueprint, render_template, redirect, url_for, request
from . import db
from .models import User
from flask_login import login_user, login_required, logout_user, current_user   
#login_user is used to login the user, login_required is used to check if the user is logged in, logout_user is used to logout the user, current_user is used to get the current user
from werkzeug.security import generate_password_hash, check_password_hash   #hash is used to store passwords in database
from flask import flash
 
auth=Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")

        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully", category="success")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password, try again", category="error")
        else:
            flash("Email does not exist", category="error")

    return render_template("login.html", title="LoginPage", user=current_user)


@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method=="POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if User.query.filter_by(email=email).first():           #checking if email exists
            flash("Email already exists", category="error")
        elif User.query.filter_by(username=username).first():   #checking if username exists
            flash("Username already exists", category="error")
        elif password1!=password2: #checking if passwords match
            flash("Passwords don't match", category="error")
        elif len(username)<2:                                   #checking if username is atleast 2
            flash("Username is too short", category="error")
        elif len(password1)<8:                                  #checking if password is atleast 8
            flash("Password is too short", category="error")
        elif len(password1)>20:                                  ##checking if password is atmost 20
            flash("Password is too long", category="error")
        elif len(email)<4:                                      #checking if email is atleast 4
            flash("Email is invalid", category="error")
        else:
            new_user=User(email=email, username=username, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("User added successfully", category="success")
            return redirect(url_for('views.home'))

    return render_template("signup.html", title="SignupPage", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash(f"Logged out successfully", category="success")
    return redirect(url_for('views.home'))