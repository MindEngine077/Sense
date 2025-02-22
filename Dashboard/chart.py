from flask import render_template
from app import app

@app.route("/chart/column-chart")
def columnChart():
    context={
        "title": "Column Chart",
        "subTitle": "Components / Column Chart",
    }
    return render_template("chart/columnChart.html", **context)
    
@app.route("/chart/line-chart")
def lineChart():
    context={
        "title": "Line Chart",
        "subTitle": "Components / Line Chart",
    }
    return render_template("chart/lineChart.html", **context)
    
@app.route("/chart/pie-chart")
def pieChart():
    context={
        "title": "Pie Chart",
        "subTitle": "Components / Pie Chart",
    }
    return render_template("chart/pieChart.html", **context)
    