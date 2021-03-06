from flask import Flask
from instance.config import DevelopmentConfig
from app.views.apis import blue_print
from app.views.user_api import blue_print_users
from flask_jwt_extended import JWTManager
import datetime
from flask_cors import CORS


def create_app():
    """The function create app allows:
            The creation of the app and gives it a name
            It also holds the configuration mode that i am working in.
            Then it takes a registered blueprint that holds the api routes
            :param config:
        """
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(DevelopmentConfig)
    app.config['JWT_SECRET_KEY'] = 'SECRET'
    JWTManager(app)
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta( minutes=200 )
    app.register_blueprint(blue_print)
    app.register_blueprint(blue_print_users)
    return app
