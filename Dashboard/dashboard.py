from flask import render_template
from app import app

@app.route("/dashboard/index2")
def index2():
    context={
        "title": "Dashboard",
        "subTitle": "CRM",
    }
    return render_template("dashboard/index2.html", **context)

@app.route("/dashboard/index3")
def index3():
    context={
        "title": "Dashboard",
        "subTitle": "eCommerce",
    }
    return render_template("dashboard/index3.html", **context)

@app.route("/dashboard/index4")
def index4():
    context={
        "title": "Dashboard",
        "subTitle": "Cryptocracy",
    }
    return render_template("dashboard/index4.html", **context)

@app.route("/dashboard/index5")
def index5():
    context={
        "title": "Dashboard",
        "subTitle": "Investment",
    }
    return render_template("dashboard/index5.html", **context)

@app.route("/dashboard/index6")
def index6():
    context={
        "title": "Dashboard",
        "subTitle": "LMS / Learning System",
    }
    return render_template("dashboard/index6.html", **context)

@app.route("/dashboard/index7")
def index7():
    context={
        "title": "Dashboard",
        "subTitle": "NFT & Gaming",
    }
    return render_template("dashboard/index7.html", **context)

@app.route("/dashboard/index8")
def index8():
    context={
        "title": "Dashboard",
        "subTitle": "Medical",
    }
    return render_template("dashboard/index8.html", **context)

@app.route("/dashboard/index9")
def index9():
    context={
        "title": "Analytics",
        "subTitle": "Analytics",
    }
    return render_template("dashboard/index9.html", **context)

@app.route("/dashboard/index10")
def index10():
    context={
        "title": "POS & Inventory",
        "subTitle": "POS & Inventory",
    }
    return render_template("dashboard/index10.html", **context)
