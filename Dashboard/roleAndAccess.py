from flask import render_template
from app import app

@app.route('/role-access/assign-role')
def assignRole():
    context={
        "title": "Role & Access",
        "subTitle": "Role & Access",
    }
    return render_template("roles_and_access/assignRole.html", **context)

@app.route('/role-access/role-access')
def roleAccess():
    context={
        "title": "Role & Access",
        "subTitle": "Role & Access",
    }
    return render_template("roles_and_access/roleAccess.html", **context)

