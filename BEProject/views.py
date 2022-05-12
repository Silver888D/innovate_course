
from flask import Blueprint, render_template, redirect, request, url_for

my_view= Blueprint('my_view',__name__)

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/contact")
def contact():
    return render_template("contact.html")

@my_view.route("/about")
def about():
    return render_template("about.html")

@my_view.route("/admin")
def admin():
    return render_template("admin.html")

@my_view.route("/example")
def example():
    return render_template("example.html")


@my_view.route("/home",)
def home_redirect():
    return redirect(url_for("my_view.index"))
    
@my_view.route("/javascript",)
def javascript_redirect():
    return redirect(url_for("my_view.index"))

@my_view.route("/js",)
def js_redirect():
    return redirect(url_for("my_view.index"))


