from flask import render_template
from app import app

@app.route('/blank-page')
def blankpage():
    context={
        "title": "Blank Page",
        "subTitle": "Blank Page",
    }
    return render_template("blankpage.html", **context)

@app.route('/calendar')
def calendar():
    context={
        "title": "Calendar",
        "subTitle": "Components / Calendar",
    }
    return render_template("calendar.html", **context)
    
@app.route('/chat')
def chat():
    context={
        "title": "Chat",
        "subTitle": "Chat",
    }
    return render_template("chat.html", **context)
    
@app.route('/chat-profile')
def chatProfile():
    context={
        "title": "Chat",
        "subTitle": "Chat",
    }
    return render_template("chatProfile.html", **context)

@app.route('/coming-soon')
def comingsoon():
    context={
        "title": "",
        "subTitle": "",
    }
    return render_template("comingsoon.html", **context)
    
@app.route('/email')
def email():
    context={
        "title": "Email",
        "subTitle": "Components / Email",
    }
    return render_template("email.html", **context)
    

@app.route('/faqs')
def faqs():
    context={
        "title": "Faq",
        "subTitle": "Faq",
    }
    return render_template("faqs.html", **context)
    
@app.route('/gallery')
def gallery():
    context={
        "title": "Gallery",
        "subTitle": "Gallery",
    }
    return render_template("gallery.html", **context)
    
@app.route('/')
def index():
    context={
        "title": "Dashboard",
        "subTitle": "AI",
    }
    return render_template("index.html", **context)
    
@app.route('/kanban')
def kanban():
    context={
        "title": "Kanban",
        "subTitle": "Kanban",
    }
    return render_template("kanban.html", **context)
    
@app.route('/maintenance')
def maintenance():
    context={
        "title": "",
        "subTitle": "",
    }
    return render_template("maintenance.html", **context)
    

@app.route('/not-found')
def notFound():
    context={
        "title": "404",
        "subTitle": "404",
    }
    return render_template("notFound.html", **context)
    
@app.route('/pricing')
def pricing():
    context={
        "title": "Pricing",
        "subTitle": "Pricing",
    }
    return render_template("pricing.html", **context)
    
@app.route('/started')
def stared():
    context={
        "title": "Email",
        "subTitle": "Components / Email",
    }
    return render_template("stared.html", **context)
    
@app.route('/terms-and-conditions')
def termsAndConditions():
    context={
        "title": "Terms & Condition",
        "subTitle": "Terms & Condition",
    }
    return render_template("termsAndConditions.html", **context)
    
@app.route('/testimonials')
def testimonials():
    context={
        "title": "Testimonials",
        "subTitle": "Testimonials",
    }
    return render_template("testimonials.html", **context)
    

@app.route('/view-details')
def viewDetails():
    context={
        "title": "Email",
        "subTitle": "Components / Email",
    }
    return render_template("viewDetails.html", **context)
    

@app.route('/widgets')
def widgets():
    context={
        "title": "Widgets",
        "subTitle": "Widgets",
    }
    return render_template("widgets.html", **context)
    