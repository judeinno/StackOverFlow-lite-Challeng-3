from app.models.User_DBmanager import DBManager
from flask_restful import Resource
from flask import request
import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


class RegisterUsers(Resource):

    def post(self):
        data = request.get_json()
        email = data['email']
        username = data['username']
        password = generate_password_hash(data['password'], method='sha256')

        if not isinstance(username, str ) or username.isspace() or username == "":
            return {"message": 'Invalid, Please enter a correct username'}, 406

        if not isinstance(password, str ) or password.isspace() or password == "":
            return {"message": 'Invalid, Please enter a correct password'}, 406

        if not re.match(r"[a-za-z0-9]+@[a-z]+", email):
            return {'message': 'Invalid email, Please check email'}, 400

        db_obj = DBManager()
        if db_obj.user_name_screening(username):
            return {'message': 'User name already exists, please select another username'}, 409
        if db_obj.email_name_screening(email):
            return {'message': 'Email already exists, please select another email'}, 409
        else:
            db_obj.create_user(data)
            return {'message': 'User successfully registered'}, 201

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        if not isinstance(username, str ) or not isinstance(password, str ):
            return {'message': 'Please enter right values'}, 400

        db_obj = DBManager()
        user = db_obj.auth_user(username)
        if user is None:
            return {'message': 'User does not exist check username'}, 400

        if not check_password_hash(user['password'], password):
            return {'message': 'Wrong password'}, 400

        access_token = create_access_token(identity=user)
        return {'access_token': access_token}, 200
