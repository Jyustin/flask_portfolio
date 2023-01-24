from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash




class test(db.Model):
    __tablename__ = 'scores'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _uid = db.Column(db.String(255), unique=True, nullable=False)
    _score = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, uid, score):
        self._uid = uid
        self._score = score

 # a getter method, extracts email from object
    @property
    def uid(self):
        return self._uid
    
    # a setter function, allows name to be updated after initial object creation
    @uid.setter
    def uid(self, uid):
        self._uid = uid
        
    # check if uid parameter matches user id in object, return boolean
    def is_uid(self, uid):
        return self._uid == uid


# a name getter method, extracts name from object
    @property
    def score(self):
        return self._score
    
    # a setter function, allows name to be updated after initial object creation
    @score.setter
    def score(self, score):
        self._score = score

 # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None


# CRUD update: updates user name, password, phone
    # returns self
    def update(self, uid="", score = ""):
        """only updates values with length"""
        if len(uid) > 0:
            self.uid = uid
        if len(score) > 0:
            self.score = score
        db.session.commit()
        return self

def initCool():
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""
    t1 = test(uid='user1', score = "10")
    t2 = test(uid='user2', score = "20")

    players = [t1, t2]
    for i in players:
        db.session.add(i) 
        db.session.commit()