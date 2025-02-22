from flask import render_template
from app import app

@app.route('/users/add-user')
def addUser():
    context={
        "title": "Add User",
        "subTitle": "Add User",
    }
    return render_template("users/addUser.html", **context)

@app.route('/users/users-grid')
def usersGrid():
    context={
        "title": "Users Grid",
        "subTitle": "Users Grid",
    }
    return render_template("users/usersGrid.html", **context)

@app.route('/users/users-list')
def usersList():
    context={
        "title": "Users List",
        "subTitle": "Users List",
    }
    return render_template("users/usersList.html", **context)

@app.route('/users/view-profile')
def viewProfile():
    context={
        "title": "View Profile",
        "subTitle": "View Profile",
    }
    return render_template("users/viewProfile.html", **context)
