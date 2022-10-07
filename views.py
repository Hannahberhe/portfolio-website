#  create my route 
from flask import Blueprint, render_template ,redirect, url_for

views = Blueprint("views",__name__,"templates")




@views.route("/")
def home():
    print("directing html")
    return render_template("index.html")
    

@views.route("/go_to_home")
def go_to_home():
    print("directing html")
    return redirect(url_for("views.home"))

@views.route("/contact")
def contact():
    print("directing contact")
    return render_template("contact.html")

@views.route("/portfolio")
def portfolio():
    print("directing portfolio")
    return render_template("portfolio.html")  


