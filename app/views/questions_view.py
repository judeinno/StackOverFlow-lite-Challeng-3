from app.models.User_DBmanager import DBManager
from flask_restful import Resource
from flask import request, current_app as app
from flask_jwt_extended import jwt_required


class QuestionManager(Resource):


    # @jwt_required
    def post(self):
        data = request.get_json()
        Question = data['Question']

        if not isinstance(Question, str ) or Question.isspace() or Question == "":
            return {"message": 'Invalid, Please enter a valid question'}, 406

        db_obj = DBManager(app.config['DATABASE_URL'])
        if db_obj.question_screening(Question):
            return {'message': 'Question already exists, please ask another question'}, 409
        else:
            db_obj.create_question(data)
            return {'message': 'You have successfully asked a question'}, 201

    # @jwt_required
    def get(self):
        db_obj = DBManager(app.config['DATABASE_URL'])
        reply = db_obj.view_questions()
        if len( reply ) <= 0:
            return {'message': 'no entry found'}, 400
        return reply, 200


class SingleQuestionManager(Resource):

    def get(self, qnId):
        db_obj = DBManager(app.config['DATABASE_URL'])
        reply = db_obj.view_question_single_id(qnId)
        return reply