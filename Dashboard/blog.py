from flask import render_template
from app import app

@app.route("/blog/add-blog")
def addBlog():
    context={
        "title": "Add Blog",
        "subTitle": "Add Blog",
    }
    return render_template("blog/addBlog.html", **context)

@app.route("/blog/blog")
def blog():
    context={
        "title": "Blog",
        "subTitle": "Blog",
    }
    return render_template("blog/blog.html", **context)

@app.route("/blog/blog-details")
def blogDetails():
    context={
        "title": "Blog Details",
        "subTitle": "Blog Details",
    }
    return render_template("blog/blogDetails.html", **context)
