import os
import datetime
import jwt
from flask import request, jsonify, make_response, abort
from werkzeug.security import generate_password_hash, check_password_hash
from app.admin.models import UserModel, USERS_LEN
from app.api.v1 import path_1 
from app.utils import validate_email, check_password

USER_KEY = os.getenv('SECRET_KEY')

@path_1.route("/auth/signup", methods=['POST'])
def user_sign_up():
    try:
        firstname = request.get_json()['firstname']
        lastname = request.get_json()['lastname']
        username = request.get_json()['username']
        email = request.get_json()['email']
        password = request.get_json()['password']
        confirm_pass = request.get_json()['confirm_password']

    except KeyError:
        abort(make_response(jsonify({'status': 400,
                                     'error': "Please check your json keys and try again"}), 400))

    check_password(password, confirm_pass)
    email = validate_email(email)

    user = User(firstname=firstname,
                username=username,
                lastname=lastname,
                email=email,
                password=password)

    #call the save_user method from the models
    user.save_user()
    return jsonify({"status":201, "data":"User Registered Successfully!"}), 201
