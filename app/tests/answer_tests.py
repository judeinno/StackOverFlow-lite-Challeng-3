import unittest
import json
from app.tests.basetest_answers import BaseTest



class TestClass(BaseTest):

    def test_invalid_answer(self):
        with self.app.test_client() as client:
            self.create_user()
            self.login_user()
            client.post( '/api/v1/questions', headers={'Content-Type': 'application/json',
                                                              'Authorization': 'Bearer ' + self.login_user()[
                                                                  'access_token']},
                                    data=json.dumps( dict( Question="What is html" ) ) )

            response = client.post( '/api/v1/questions/1/answers', headers={'Content-Type': 'application/json',
                                                                  'Authorization': 'Bearer ' + self.login_user()[
                                                                      'access_token']},
                                    data=json.dumps( dict( Answer=" " ) ) )
            responseJson = json.loads( response.data.decode() )
            self.assertIn( 'Invalid, Please enter a valid answer', responseJson['message'] )

    def test_add_answer(self):
        with self.app.test_client() as client:
            self.create_user()
            self.login_user()
            client.post( '/api/v1/questions', headers={'Content-Type': 'application/json',
                                                              'Authorization': 'Bearer ' + self.login_user()[
                                                                  'access_token']},
                                    data=json.dumps( dict( Question="What is html" ) ) )

            response = client.post( '/api/v1/questions/1/answers', headers={'Content-Type': 'application/json',
                                                                  'Authorization': 'Bearer ' + self.login_user()[
                                                                      'access_token']},
                                    data=json.dumps( dict( Answer="Ok" ) ) )
            responseJson = json.loads( response.data.decode() )
            self.assertIn( 'answer successfully created', responseJson['message'] )

    def test_modify_answer_to_prefered(self):
        with self.app.test_client() as client:
            self.create_user()
            self.login_user()
            client.post( '/api/v1/questions', headers={'Content-Type': 'application/json',
                                                              'Authorization': 'Bearer ' + self.login_user()[
                                                                  'access_token']},
                                    data=json.dumps( dict( Question="What is html" ) ) )

            client.post( '/api/v1/questions/1/answers', headers={'Content-Type': 'application/json',
                                                                  'Authorization': 'Bearer ' + self.login_user()[
                                                                      'access_token']},
                                    data=json.dumps( dict( Answer="Ok" ) ) )
            response = client.put( '/api/v1/questions/1/answers/1', headers={'Content-Type': 'application/json',
                                                                            'Authorization': 'Bearer ' +
                                                                                             self.login_user()[
                                                                                                 'access_token']},
                                    data=json.dumps( dict() ) )
            responseJson = json.loads( response.data.decode() )
            self.assertIn( 'Answer approved', responseJson['message'] )

    def test_modify_answer_by_ans_auth(self):
        with self.app.test_client() as client:
            self.create_user()
            self.login_user()
            client.post( '/api/v1/questions', headers={'Content-Type': 'application/json',
                                                              'Authorization': 'Bearer ' + self.login_user()[
                                                                  'access_token']},
                                    data=json.dumps( dict( Question="What is html" ) ) )
            self.client().post( '/api/v1/auth/signup',
                                data=json.dumps( self.user_reg_sec ),
                                content_type='application/json' )
            login_response = self.client().post( '/api/v1/auth/login',
                                                 data=json.dumps( self.loginlist_sec ),
                                                 content_type='application/json' )
            login_result = json.loads( login_response.data.decode() )
            client.post( '/api/v1/questions/1/answers', headers={'Content-Type': 'application/json',
                                                                  'Authorization': 'Bearer ' + login_result[
                                                                      'access_token']},
                                    data=json.dumps( dict( Answer="Ok" ) ) )
            response = client.put( '/api/v1/questions/1/answers/1', headers={'Content-Type': 'application/json',
                                                                            'Authorization': 'Bearer ' +
                                                                                             login_result[
                                                                                                 'access_token']},
                                    data=json.dumps( dict(Answers="Fine") ) )
            responseJson = json.loads( response.data.decode() )
            self.assertIn( 'Answer edited', responseJson['message'] )


if __name__ == '__main__':
    unittest.main()