import unittest
import json
from app.tests.Basetest import BaseTest


class TestClass(BaseTest):



    def test_user_siginup(self):
        """Test API can signup """

        res = self.client().post('/api/v1/auth/signup',
                                 content_type='application/json',
                                 data=json.dumps(self.user_reg))
        self.assertTrue(res.status_code, 201)
        self.assertIn('User successfully registered', str(res.data))

    def test_user_siginup_incorrect_user_name(self):
        """Test API can signup user_name"""

        res = self.client().post('/api/v1/auth/signup',
                                 content_type='application/json',
                                 data=json.dumps({
                                                "username": "",
                                                "email": "ude@sample.com",
                                                "password": "password"
                                                }))
        self.assertTrue(res.status_code, 201)
        self.assertIn('Invalid, Please enter a correct username', str(res.data))

    def test_user_siginup_incorrect_email(self):
        """Test API can signup incorrect_email"""

        res = self.client().post('/api/v1/auth/signup',
                                 content_type='application/json',
                                 data=json.dumps({
                                                "username": "ude",
                                                "email": "Jude@sample.com",
                                                "password": "password"
                                                }))
        self.assertTrue(res.status_code, 201)
        self.assertIn('Invalid email, Please check email', str(res.data))

    def test_user_siginup_user_already_exissts(self):
        """Test API can signup already_exissts"""

        self.client().post('/api/v1/auth/signup',
                                 content_type='application/json',
                                 data=json.dumps({
                                                "username": "ude",
                                                "email": "ude@sample.com",
                                                "password": "password"
                                                }))
        res = self.client().post( '/api/v1/auth/signup',
                                  content_type='application/json',
                                  data=json.dumps( {
                                      "username": "ude",
                                      "email": "ude@sample.com",
                                      "password": "password"
                                  } ) )
        self.assertTrue(res.status_code, 409)
        self.assertIn('User name already exists, please select another username', str(res.data))

    def test_user_siginup_user_email_already_exists(self):
        """Test API can signup user_already_exists"""

        self.client().post('/api/v1/auth/signup',
                                 content_type='application/json',
                                 data=json.dumps({
                                                "username": "jude",
                                                "email": "ude@sample.com",
                                                "password": "password"
                                                }))
        res = self.client().post( '/api/v1/auth/signup',
                                  content_type='application/json',
                                  data=json.dumps( {
                                      "username": "ude",
                                      "email": "ude@sample.com",
                                      "password": "password"
                                  } ) )
        self.assertTrue(res.status_code, 409)
        self.assertIn('Email already exists, please select another email', str(res.data))

    def test_login_user_(self):
        with self.app.test_client() as client:
            self.client().post( '/api/v1/auth/signup',
                                content_type='application/json',
                                data=json.dumps( self.user_reg ) )
            login_response = client.post( '/api/v1/auth/login', content_type='application/json',
                                          data=json.dumps( self.user_reg ) )
            login_result = json.loads( login_response.data.decode() )
            self.assertEqual( login_response.status_code, 200 )

    def test_login_that_doesnt_exist(self):
        with self.app.test_client() as client:
            res = login_response = client.post( '/api/v1/auth/login', content_type='application/json',
                                          data=json.dumps( {
                                      "username": "ude",
                                      "email": "ude@sample.com",
                                      "password": "password"
                                  } ) )
            self.assertEqual( login_response.status_code, 400 )
            self.assertIn( 'Please either register, enter right values or User does not exist', str( res.data ) )

    def test_login_user_wrong_password(self):
        with self.app.test_client() as client:
            self.client().post( '/api/v1/auth/signup',
                                content_type='application/json',
                                data=json.dumps( {
                                      "username": "ude",
                                      "email": "ude@sample.com",
                                      "password": "password"
                                  } ) )
            login_response = client.post( '/api/v1/auth/login', content_type='application/json',
                                          data=json.dumps( {
                                      "username": "ude",
                                      "email": "ude@sample.com",
                                      "password": "passwo"
                                  } ) )
            login_result = json.loads( login_response.data.decode() )
            self.assertEqual( login_response.status_code, 400 )
            self.assertIn( 'Wrong password', str( login_response.data ) )


if __name__ == '__main__':
    unittest.main()