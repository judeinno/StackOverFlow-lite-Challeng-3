from flask import Blueprint
from flask_restplus import Api
from app.views.user_views import RegisterUsers, Login


# Initialistion of blueprint, giving it a name and a url prefix
blue_print_users = Blueprint('user_Bp', __name__, url_prefix='/api/v1')

# Making the blueprint an instance of the class Api
api = Api(blue_print_users)


api.add_resource(RegisterUsers, '/auth/signup')
api.add_resource(Login, '/auth/login')