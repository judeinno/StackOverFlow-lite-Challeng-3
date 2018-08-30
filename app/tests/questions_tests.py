import unittest
import json
from app.tests.Basetest import BaseTest



class TestClass(BaseTest):

    def test_add_new_question(self):
        with self.app.test_client() as client:
            self.create_user()
            self.login_user()
            response = client.post( '/api/v1/questions', headers={'Content-Type': 'application/json',
                                                              'Authorization': 'Bearer ' + self.login_user()[
                                                                  'access_token']},
                                    data=json.dumps( dict( Question="What is html" ) ) )

            self.assertEqual( response.status_code, 201 )
            responseJson = json.loads( response.data.decode() )
            self.assertIn( 'You have successfully asked a question', responseJson['message'] )

    def test_question_exists(self):
        with self.app.test_client() as client:
            self.create_user()
            self.login_user()
            client.post( '/api/v1/questions', headers={'Content-Type': 'application/json',
                                                                  'Authorization': 'Bearer ' + self.login_user()[
                                                                      'access_token']},
                                    data=json.dumps( dict( Question="What is html" ) ) )
            response = client.post( '/api/v1/questions', headers={'Content-Type': 'application/json',
                                                              'Authorization': 'Bearer ' + self.login_user()[
                                                                  'access_token']},
                                    data=json.dumps( dict( Question="What is html" ) ) )

            self.assertEqual( response.status_code, 409 )
            responseJson = json.loads( response.data.decode() )
            self.assertIn( 'Question already exists, please ask another question', responseJson['message'] )

    def test_question_invalid(self):
        with self.app.test_client() as client:
            self.create_user()
            self.login_user()
            response = client.post( '/api/v1/questions', headers={'Content-Type': 'application/json',
                                                              'Authorization': 'Bearer ' + self.login_user()[
                                                                  'access_token']},
                                    data=json.dumps( dict( Question="" ) ) )

            self.assertEqual( response.status_code, 406 )
            responseJson = json.loads( response.data.decode() )
            self.assertIn( 'Invalid, Please enter a valid question', responseJson['message'] )

    def test_question_get(self):
        with self.app.test_client() as client:
            self.create_user()
            self.login_user()
            client.post( '/api/v1/questions', headers={'Content-Type': 'application/json',
                                                              'Authorization': 'Bearer ' + self.login_user()[
                                                                  'access_token']},
                                    data=json.dumps( dict( Question="What is html" ) ) )
            response = client.get( '/api/v1/questions', content_type='application/json' )
            responseJson = json.loads( response.data.decode() )
            self.assertEqual( "What is html", responseJson[0]["Question"] )
            self.assertEqual( response.status_code, 200 )

    def test_get_question_that_doesnt_exist(self):
        with self.app.test_client() as client:
            self.create_user()
            self.login_user()
            response = client.get( '/api/v1/questions', content_type='application/json',
                                    data=json.dumps( dict( Question="What is html" ) ) )
            responseJson = json.loads( response.data.decode() )
            self.assertEqual( response.status_code, 400 )
            self.assertIn( 'no entry found', responseJson['message'] )


if __name__ == '__main__':
    unittest.main()