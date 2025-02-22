from flask import render_template
from app import app

@app.route('/invoice/add-new')
def addNew():
    context={
        "title": "Invoice List",
        "subTitle": "Invoice List",
    }
    return render_template("invoice/addNew.html", **context)
    
@app.route('/invoice/edit')
def edit():
    context={
        "title": "Invoice List",
        "subTitle": "Invoice List",
    }
    return render_template("invoice/edit.html", **context)
    
@app.route('/invoice/invoice-list')
def invoiceList():
    context={
        "title": "Invoice List",
        "subTitle": "Invoice List",
    }
    return render_template("invoice/list.html", **context)
    
@app.route('/invoice/preview')
def preview():
    context={
        "title": "Invoice List",
        "subTitle": "Invoice List",
    }
    return render_template("invoice/preview.html", **context)
    