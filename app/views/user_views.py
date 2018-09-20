from app.models.User_DBmanager import DBManager
from flask_restful import Resource
from app.models.model import User
import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import request, current_app as app
from flasgger import swag_from


class RegisterUsers(Resource):

    @swag_from( 'user_views.yml', methods=['POST'] )
    def post(self):
        """Register a user.

        Allows a user to sign up.
        """
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

        db_obj = DBManager(app.config['DATABASE_URL'])
        if db_obj.user_name_screening(username):
            return {'message': 'User name already exists, please select another username'}, 409
        if db_obj.email_name_screening(email):
            return {'message': 'Email already exists, please select another email'}, 409
        else:
            db_obj.create_user(data)
            return {'message': 'User successfully registered'}, 201

class Login(Resource):

    @swag_from('login.yml', methods=['POST'])
    def post(self):
        """Login a user.

        Allows a user to sign in.
        """
        data = request.get_json()
        username = data['username']
        password = data['password']


        db_obj = DBManager(app.config['DATABASE_URL'])
        user = db_obj.auth_user(username)
        query = db_obj.fetch_by_param(
            'users', 'username', data['username'] )
        if not query:
            return {'message': 'Please either register, enter right values or User does not exist'}, 400
        the_user = User( query[0], query[1], query[2], query[3] )
        if  check_password_hash(user['password'], password) and the_user.username == data['username']:
            access_token = create_access_token( identity=user )
            return {'access_token': access_token}, 200
        else:
            return {'message': 'Wrong password'}, 400


