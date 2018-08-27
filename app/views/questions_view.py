from app.models.User_DBmanager import DBManager
from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required


class QuestionManager(Resource):


    # @jwt_required
    def post(self):
        data = request.get_json()
        Question = data['Question']

        if not isinstance(Question, str ) or Question.isspace() or Question == "":
            return {"message": 'Invalid, Please enter a valid question'}, 406

        db_obj = DBManager()
        if db_obj.question_screening(Question):
            return {'message': 'Question already exists, please ask another question'}, 409
        else:
            db_obj.create_question(data)
            return {'message': 'You have successfully asked a question'}, 201

    # @jwt_required
    def get(self):
        db_obj = DBManager()
        reply = db_obj.view_questions()
        if len( reply ) <= 0:
            return {'message': 'no entry found'}, 400
        return reply, 200