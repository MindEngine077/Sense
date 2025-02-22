from flask import render_template
from app import app

@app.route('/table/basic-table')
def basicTable():
    context={
        "title": "Basic Table",
        "subTitle": "Basic Table",
    }
    return render_template("table/basicTable.html", **context)

@app.route('/table/data-table')
def dataTable():
    context={
        "title": "Data Table",
        "subTitle": "Data Table",
    }
    return render_template("table/dataTable.html", **context)
