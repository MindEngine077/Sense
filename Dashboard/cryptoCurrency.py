from flask import render_template
from app import app

@app.route("/crypto-currency/marketplace")
def marketplace():
    context={
        "title": "Market Place",
        "subTitle": "Market Place",
    }
    return render_template("crypto_currency/marketplace.html", **context)

@app.route("/crypto-currency/marketplace-details")
def marketplaceDetails():
    context={
        "title": "Market Place Details",
        "subTitle": "Market Place Details",
    }
    return render_template("crypto_currency/marketplaceDetails.html", **context)

@app.route("/crypto-currency/portfolio")
def portfolio():
    context={
        "title": "Portfolio",
        "subTitle": "Portfolio",
    }
    return render_template("crypto_currency/portfolio.html", **context)

@app.route("/crypto-currency/wallet")
def wallet():
    context={
        "title": "Wallet",
        "subTitle": "Wallet",
    }
    return render_template("crypto_currency/wallet.html", **context)
