import os
import datetime
import uuid
from run import db, app
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """This class represents the user table."""
    __tablename__='Users'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(str(uuid.uuid4()))
    email = db.Column(db.String(120), nullable=False, unique=True)
    username = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    

class Shopping_list(db.Model):
    __tablename__ = 'Shopping_list'

    id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String(50))
    list_id = db.Column(str(uuid.uuid4()))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    # items = db.relationship(
    #     'Items'

    # )

class Items(db.Model):
    __tablename__= 'Items'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50))
    item_id = db.Column(str(uuid.uuid4()))    
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

@app.route('/users', methods=['GET'])
def get_all_users():
    return ''

@app.route('/users/<user_id>', methods=['GET'])
def get_one_user(user_id):
    return ''

@app.route('/users', methods=['POST'])
def create_user():
    return ''

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    return ''

