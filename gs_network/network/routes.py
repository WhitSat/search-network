from network import app 
from flask import render_template
from network.models import Satellite

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/search")
def search_page():
    satellites = Satellite.query.all()
    return render_template('search.html', satellites = satellites)