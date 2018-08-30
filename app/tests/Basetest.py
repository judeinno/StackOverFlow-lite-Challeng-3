import unittest
from app import create_app
from app.models.User_DBmanager import DBManager
import json
from instance.config import TestingConfig
from flask import current_app as app

class BaseTest (unittest.TestCase):

    def creating_app(self):
        app = create_app()
        app.config.from_object(TestingConfig)
        return app

    def setUp(self):
        self.app = self.creating_app()
        self.client = self.app.test_client
        self.app.app_context().push()
        db = DBManager(app.config['DATABASE_URL'])
        db.create_tables()

        self.user_reg = {
            "username": "jude",
            "email": "jude@sample.com",
            "password": "password"
        }

        self.loginlist = {
            'username': 'jude',
            'password': 'password'
        }

    def create_user(self):
        response = self.client().post( '/api/v1/auth/signup',
                                       data=json.dumps( self.user_reg ),
                                       content_type='application/json' )
        return response

    def login_user(self):
        login_response = self.client().post( '/api/v1/auth/login',
                                       data=json.dumps( self.loginlist ),
                                       content_type='application/json' )
        login_result = json.loads( login_response.data.decode() )
        return login_result

    def tearDown(self):
        db = DBManager(app.config['DATABASE_URL'])
        db.trancate_table()