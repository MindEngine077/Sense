from flask import render_template
from app import app

@app.route('/forms/form-validation')
def formValidation():
    context={
        "title": "Form Validation",
        "subTitle": "Form Validation",
    }
    return render_template("forms/formValidation.html", **context)

@app.route('/forms/form-wizard')
def formWizard():
    context={
        "title": "Wizard",
        "subTitle": "Wizard",
    }
    return render_template("forms/formWizard.html", **context)

@app.route('/forms/input-forms')
def inputForms():
    context={
        "title": "Input Forms",
        "subTitle": "Input Forms",
    }
    return render_template("forms/inputForms.html", **context)

@app.route('/forms/input-layout')
def inputLayout():
    context={
        "title": "Input Layout",
        "subTitle": "Input Layout",
    }
    return render_template("forms/inputLayout.html", **context)
