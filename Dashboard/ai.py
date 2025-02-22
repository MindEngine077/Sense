from flask import render_template
from app import app

@app.route('/ai/code-generator')
def codeGenerator():
    context={
        "title": "Code Generator",
        "subTitle": "Code Generator",
    }
    return render_template("ai/codeGenerator.html", **context)

@app.route('/ai/code-generator-new')
def codeGeneratorNew():
    context={
        "title": "Code  Generator",
        "subTitle": "Code  Generator",
    }
    return render_template("ai/codeGeneratorNew.html", **context)

@app.route('/ai/image-generator')
def imageGenerator():
    context={
        "title": "Image  Generator",
        "subTitle": "Image  Generator",
    }
    return render_template("ai/imageGenerator.html", **context)

@app.route('/ai/text-generator')
def textGenerator():
    context={
        "title": "Text Generator",
        "subTitle": "Text Generator",
    }
    return render_template("ai/textGenerator.html", **context)

@app.route('/ai/text-generator-new')
def textGeneratorNew():
    context={
        "title": "Text Generator",
        "subTitle": "Text Generator",
    }
    return render_template("ai/textGeneratorNew.html", **context)

@app.route('/ai/video-generator')
def videoGenerator():
    context={
        "title": "Video Generator",
        "subTitle": "Video Generator",
    }
    return render_template("ai/videoGenerator.html", **context)

@app.route('/ai/voice-generator')
def voiceGenerator():
    context={
        "title": "Voice Generator",
        "subTitle": "Voice Generator",
    }
    return render_template("ai/voiceGenerator.html", **context)
