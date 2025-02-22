from flask import render_template
from app import app

@app.route("/components/accordion")
def alerts():
    context={
        "title": "Alerts",
        "subTitle": "Components / Alerts",
    }
    return render_template("components/alerts.html", **context)
    
@app.route("/components/avatar")
def avatars():
    context={
        "title": "Avatars",
        "subTitle": "Components / Avatars",
    }
    return render_template("components/avatars.html", **context)
    
@app.route("/components/badges")
def badges():
    context={
        "title": "Badges",
        "subTitle": "Components / Badges",
    }
    return render_template("components/badges.html", **context)
    
@app.route("/components/button")
def button():
    context={
        "title": "Button",
        "subTitle": "Components / Button",
    }
    return render_template("components/button.html", **context)
    
@app.route("/components/calendar")
def calendarMain():
    context={
        "title": "Calendar",
        "subTitle": "Components / Calendar",
    }
    return render_template("components/calendar.html", **context)
    
@app.route("/components/card")
def card():
    context={
        "title": "Card",
        "subTitle": "Components / Card",
    }
    return render_template("components/card.html", **context)
    
@app.route("/components/carousel")
def carousel():
    context={
        "title": "Carousel",
        "subTitle": "Components / Carousel",
    }
    return render_template("components/carousel.html", **context)
    
@app.route("/components/color")
def colors():
    context={
        "title": "Colors",
        "subTitle": "Components / Colors",
    }
    return render_template("components/colors.html", **context)
    
@app.route("/components/dropdown")
def dropdown():
    context={
        "title": "Dropdown",
        "subTitle": "Components / Dropdown",
    }
    return render_template("components/dropdown.html", **context)
    
@app.route("/components/list")
def list():
    context={
        "title": "List",
        "subTitle": "Components / List",
    }
    return render_template("components/list.html", **context)
    
@app.route("/components/pagination")
def pagination():
    context={
        "title": "Pagination",
        "subTitle": "Components / Pagination",
    }
    return render_template("components/pagination.html", **context)

@app.route("/components/progressbar")
def progressbar():
    context={
        "title": "Progressbar",
        "subTitle": "Components / Progressbar",
    }
    return render_template("components/progressbar.html", **context)
    
@app.route("/components/radio")
def radio():
    context={
        "title": "Radio",
        "subTitle": "Components / Radio",
    }
    return render_template("components/radio.html", **context)
    
@app.route("/components/ratings")
def starRatings():
    context={
        "title": "Star Ratings",
        "subTitle": "Components / Star Ratings",
    }
    return render_template("components/starRatings.html", **context)
    
@app.route("/components/switch")
def switch():
    context={
        "title": "Switch",
        "subTitle": "Components / Switch",
    }
    return render_template("components/switch.html", **context)
    
@app.route("/components/tab-accordion")
def tabAndAccordion():
    context={
        "title": "Tab & Accordion",
        "subTitle": "Components / Tab & Accordion",
    }
    return render_template("components/tabAndAccordion.html", **context)
    
@app.route("/components/tags")
def tags():
    context={
        "title": "Tags",
        "subTitle": "Components / Tags",
    }
    return render_template("components/tags.html", **context)
    
@app.route("/components/tooltip")
def tooltip():
    context={
        "title": "Tooltip & Popover",
        "subTitle": "Components / Tooltip & Popover",
    }
    return render_template("components/tooltip.html", **context)
    
@app.route("/components/typography")
def typography():
    context={
        "title": "Typography",
        "subTitle": "Components / Typography",
    }
    return render_template("components/typography.html", **context)
    
@app.route("/components/file-upload")
def upload():
    context={
        "title": "File Upload",
        "subTitle": "Components / File Upload",
    }
    return render_template("components/upload.html", **context)
    
@app.route("/components/videos")
def videos():
    context={
        "title": "Videos",
        "subTitle": "Components / Videos",
    }
    return render_template("components/videos.html", **context)
    