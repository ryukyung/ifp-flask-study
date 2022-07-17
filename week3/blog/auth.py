# blog/auth.py
from flask import Blueprint, render_template, redirect

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return redirect("views.blog_home")

@auth.route("/sign-up")
def signup():
    return render_template("signup.html")