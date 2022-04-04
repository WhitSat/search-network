from network import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(length=30), nullable = False, unique = True)
    email_address = db.Column(db.String(length=50), nullable = False, unique = True)
    password_hash = db.Column(db.String(length=60), nullable = False)

class Satellite(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    source = db.Column(db.String(length = 50), nullable = False)
    name = db.Column(db.String(length = 24), nullable = False, unique = True)
    norad_id = db.Column(db.Integer(), nullable = False, unique = True)
    launch_year = db.Column(db.Integer(), nullable = False)
    inclination = db.Column(db.Float(), nullable = False)
    eccentricity = db.Column(db.Float(), nullable = False)
    apogee = db.Column(db.Float(), nullable = False)
    epoch_age = db.Column(db.Float(), nullable = False)
    
    def __repr__(self):
        return f'satellite {self.name}'
