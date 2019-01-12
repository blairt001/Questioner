#This module contains the functions that will validate users data
#imports
import os
import re
from functools import wraps
import jwt
from flask import jsonify, request, abort, make_response
from werkzeug.security import generate_password_hash

# local imports
from app.admin.models import UserModel, USERS_LEN

key = os.getenv("SECRET_KEY")

def check_password(password, confirmed_password):
  
    '''
     Lets check if our passoword meets the requirements
    '''
        # check to confirm the password is of required length
    if len(password) < 8 or len(password) > 20:
        abort(make_response(jsonify(error="Password should not be less than 8 characters or exceed 20"), 400))

    # check if password contains at least an alphabet(a-z)
    if not re.search("[a-z]", password):
        abort(make_response(jsonify(error="Password should contain a letter between a-z"), 400))

    # check if password contains at least an upper case letter
    if not re.search("[A-Z]", password):
        abort(make_response(jsonify(error="Password should contain a capital letter"), 400))

    # check if password contains at least a number(0-9)
    if not re.search("[0-9]", password):
        abort(make_response(jsonify(error="Password should contain a number(0-9)"), 400))

    # Checks if passwords provided by the users match
    if password != confirmed_password:
        abort(make_response(jsonify(error="Your passwords don't match!"), 400))

    # If they match..
    hashed_password = generate_password_hash(password, method='sha256')

    return hashed_password

#validate email
def validate_email(email):
    """
    Is the email valid , is it already used?
    """

    for user in USERS_LEN:
        if email == user.email:
            abort(make_response(jsonify(error="Email is already taken!"), 400))
    try:
        user, domain = str(email).split("@")
    except ValueError:
        abort(make_response(jsonify(error="Email is Invalid"), 400))
    if not user or not domain:
        abort(make_response(jsonify(error="Email is Invalid"), 400))

    # Is the domain you are using valid?
    try:
        dom1, dom2 = domain.split(".")
    except ValueError:
        abort(make_response(jsonify(error="Email is Invalid"), 400))
    if not dom1 or not dom2:
        abort(make_response(jsonify(error="Email is Invalid"), 400))

    return email

#wrap our function and check for the access-token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message':"Access Token is missing"}), 401

        try:
            data = jwt.decode(token, key)
            current_user = None
            for user in USERS_LEN:
                if user.username == data['username']:
                    current_user = user

        except:
            return jsonify({'message':'The token is expired or invalid'}), 401

        return f(current_user, *args, **kwargs)
    return decorated

#lets decode our token back
def decode_token():
    token = request.headers['x-access-token']
    try:
        username = jwt.decode(token, key)
    except:
        return jsonify({"message":"The token is expired or invalid"}), 401

    return username

#lests verify if the user is an admin or not
    def verify_if_user_is_admin(username):
    admin = None
    for user in USERS_LEN:
        if username == 'blairtheadmin':
            user.is_admin = True
            admin = True
        admin = False
    return admin

#check if the user is actually an admin
def check_if_user_is_admin():
    username = decode_token()
    if username['username'] != "blairtheadmin":
        return False
    return True