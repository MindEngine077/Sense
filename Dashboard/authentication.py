from flask import render_template
from app import app

@app.route("/authentication/forgot-password")
def forgotPassword():
    return render_template("authentication/forgotPassword.html")

@app.route("/authentication/signin")
def signin():
    return render_template("authentication/signin.html")

@app.route("/authentication/signup")
def signup():
    return render_template("authentication/signup.html")
