from unicodedata import name
from flask import Blueprint, render_template, redirect, request, url_for
from favourites import empty, add_to_list, delete_from_list
my_view= Blueprint('my_view',__name__)

@my_view.route("/")
def home():
    return render_template("home.html")

@my_view.route("/contact")
def contact():
    return render_template("contact.html")

@my_view.route("/about", methods=["GET","POST"])
def about():
    if request.method == "POST":
        try:
            id == "song_add"
            new_song = request.form["add_song"]
            add_to_list(new_song)
        except:
            id == "song_delete"
            remove_song = request.form["delete_song"]
            delete_from_list(remove_song)
    return render_template("about.html", songs=empty)

@my_view.route("/home",)
def home_redirect():
    return redirect(url_for("my_view.home"))
@my_view.route("/homepage",)
def homepage_redirect():
    return redirect(url_for("my_view.home"))