from flask import Blueprint, render_template ,redirect, url_for

views = Blueprint(__name__,"views")




@views.route("/home")
def home():
    return render_template("index.html")
    

@views.route("/go_to_home")
def go_to_home():
    return redirect(url_for("views.home"))

@views.route("/contact")
def contact():
    return render_template("contact.html")

@views.route("/portfolio")
def portfolio():
    return render_template("index.html")   