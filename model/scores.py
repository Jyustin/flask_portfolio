from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


def initCool():
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""
    u1 = ("ok")
    cool = [u1]