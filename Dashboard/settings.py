from flask import render_template
from app import app

@app.route('/settings/company')
def company():
    context={
        "title": "Company",
        "subTitle": "Settings - Company",
    }
    return render_template("settings/company.html", **context)

@app.route('/settings/currencies')
def currencies():
    context={
        "title": "Currrencies",
        "subTitle": "Settings - Currencies",
    }
    return render_template("settings/currencies.html", **context)

@app.route('/settings/languages')
def languages():
    context={
        "title": "Languages",
        "subTitle": "Settings - Languages",
    }
    return render_template("settings/languages.html", **context)

@app.route('/settings/notification')
def notification():
    context={
        "title": "Notification",
        "subTitle": "Settings - Notification",
    }
    return render_template("settings/notification.html", **context)

@app.route('/settings/notification-alert')
def notificationAlert():
    context={
        "title": "Notification Alert",
        "subTitle": "Settings - Notification Alert",
    }
    return render_template("settings/notificationAlert.html", **context)

@app.route('/settings/payment-getway')
def paymentGetway():
    context={
        "title": "Payment Getway",
        "subTitle": "Settings - Payment Getway",
    }
    return render_template("settings/paymentGetway.html", **context)

@app.route('/settings/theme')
def theme():
    context={
        "title": "Theme",
        "subTitle": "Settings - Theme",
    }
    return render_template("settings/theme.html", **context)
