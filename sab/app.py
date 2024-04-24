from flask import Flask 
from flask import render_template
app = Flask("mon app")

@app.route("/")
def accueil():
    return render_template("index.html")