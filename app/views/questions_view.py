from app.models.User_DBmanager import DBManager
from flask_restplus import Resource
from flask import request, current_app as app
from flask_jwt_extended import jwt_required, get_jwt_identity


class QuestionManager(Resource):


    @jwt_required
    def post(self):
        """Post a question.

        Allows a user to post a question.
        """
        data = request.get_json()
        Question = data['Question']
        userid_current = get_jwt_identity()
        current_user = userid_current['userId']

        if not isinstance(Question, str ) or Question.isspace() or Question == "":
            return {"message": 'Invalid, Please enter a valid question'}, 406

        db_obj = DBManager(app.config['DATABASE_URL'])
        my_user_check = db_obj.fetch_by_specific_param( 'userId', 'users', 'userId', current_user )
        if db_obj.question_screening(Question):
            return {'message': 'Question already exists, please ask another question'}, 409

        if my_user_check:
            db_obj.create_question(current_user, data)
            return {'message': 'You have successfully asked a question'}, 201


    def get(self):
        """Get all questions.

        Allows a user to get all questions.
        """
        db_obj = DBManager(app.config['DATABASE_URL'])
        reply = db_obj.view_questions()
        if len( reply ) <= 0:
            return {'message': 'no entry found'}, 400
        return reply, 200


class SingleQuestionManager(Resource):

    @jwt_required
    def get(self, qnId):
        """Get a question by id.

        Allows a user to get a question by id.
        """
        db_obj = DBManager(app.config['DATABASE_URL'])
        reply = db_obj.view_question_single_id(qnId)
        return reply


class DeleteQuestionManager(Resource):

    @jwt_required
    def delete(self, qnId):
        """Delete a question by id.

        Allows a user to delete a question by id.
        """
        db_obj = DBManager( app.config['DATABASE_URL'] )
        userid_current = get_jwt_identity()
        current_user = userid_current['userId']
        my_user_check = db_obj.fetch_by_specific_param('userId', 'users', 'userId', current_user)
        if my_user_check:
            if db_obj.delete_question( qnId ):
                return 202
            return {'message': 'Question deleted successfully'}, 202