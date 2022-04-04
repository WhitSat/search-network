from enum import unique
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from numpy import source

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///network.db'
db = SQLAlchemy(app)

from network import routes