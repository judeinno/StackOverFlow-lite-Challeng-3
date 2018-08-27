import unittest
from instance.config import TestingConfig
from app import create_app
from app.models.model import Questions
import json


class BaseCase(unittest.TestCase):
    """The class holds the:
        -Method to set up the tests where i create the app,
        -also initialise the client method
        -plus the test dummy data
        -It also holds all the unittests for the app
    """

    def setUp(self):
        """
        The method set up sets up the app by:
         -creating the app
         -Also initialises the client where tests will be run
         -It also provides some dummy data to be used in some tests.
        """
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()


    def test_model_function(self):
        """Tests if the dummy data provided is
            an instance of the class Question
        """
        self.question = Questions( qn_id=1, question="What is html" )
        self.assertIsInstance(self.question, Questions)

    def test_all_question(self):
        """
        Test get:
        -It check if the url provides data in index 0 with id=1
        -And that the response code is 200 for Ok
        """
        with self.client as client:
            response = client.get("/api/v1/questions",
                                  content_type="application/json",
                                  data=json.dumps(dict()))
            response_json = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)

    def test_question_post(self):
        """
            Test post:
            -And then tests that the response code is 201 for Created
            -And also test that the correct response message
        """
        with self.client as client:
            response = client.post("/api/v1/questions", content_type="application/json",
                                   data=json.dumps(dict(question="What is html in full")))
            response_json = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('Question Added successfully', response_json['message'])

    def test_question_invalid_post(self):
        """
           Test post
           -the post method returns an invalid message if an int is entered
           -And also test that the correct response message
       """
        with self.client as client:
            response = client.post("/api/v1/questions", content_type="application/json",
                                   data=json.dumps(dict(question=112,
                                                          answer=[])))
            responseJson = json.loads(response.data.decode())
            self.assertIn('Invalid, Please make sure your asking the question well', responseJson['message'])

    def test_single_question(self):
        """
           Test get:
           -the get method that gets a single question
           -It check if the url provides data in index 0 with id=1
           -And also test that the correct response code is returned
       """
        with self.client as client:
            response = client.get("/api/v1/questions/1",
                                  content_type="application/json",
                                  data=json.dumps( dict( qn_id=1)))
            response_json = json.loads(response.data.decode())
            self.assertEqual(1, response_json[0]["qn_id"])
            self.assertEqual(response.status_code, 200)

    def test_answer_post(self):
        """
           Test post:
           -the post method that posts an answer
           -And also test that the correct response code is returned
           -Plus the correct response message
       """
        with self.client as client:
            client.post( "/api/v1/questions",
                        content_type="application/json",
                        data=json.dumps( dict(question="What is html in full") ) )
            client.get( "/api/v1/questions/1",
                        content_type="application/json",
                        data=json.dumps( dict( qn_id=1 ) ) )
            response = client.post("/api/v1/questions/1/answers",
                                   content_type="application/json",
                                   data=json.dumps(dict(answer='Hyper text transfer protocal')))
            self.assertEqual(response.status_code, 201)
            response_json = json.loads(response.data.decode())
            self.assertIn('Answer successfully added', response_json['message'])

    def test_answer_invalid_post(self):
        """
           Test post:
           -the post method returns an invalid message if an int is entered
           -And also test that the correct response message
       """
        with self.client as client:
            response = client.post("/api/v1/questions/1/answers", content_type="application/json",
                                    data=json.dumps(dict( answer=123)))
            responseJson = json.loads( response.data.decode() )
            self.assertIn('Invalid, Please make sure you posted the answer well', responseJson['message'])

if __name__ == '__main__':
    unittest.main()