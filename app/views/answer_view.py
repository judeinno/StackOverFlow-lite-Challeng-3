from app.models.User_DBmanager import DBManager
from flask_restful import Resource
from flask import request, current_app as app
from flask_jwt_extended import jwt_required, get_jwt_identity



class AnswerManager(Resource):

    @jwt_required
    def post(self, qnId):
        userid_current = get_jwt_identity()
        current_user = userid_current['userId']
        data = request.get_json()
        Answer = data['Answer']
        db_obj = DBManager( app.config['DATABASE_URL'] )
        if not isinstance(Answer, str ) or Answer.isspace() or Answer == "":
            return {"message": 'Invalid, Please enter a valid question'}, 406
        db_obj.fetch_question_value(qnId)
        db_obj.create_answer(qnId, current_user, data)
        return {'message': 'answer successfully created'}

class UpdateAnswer(Resource):

    @jwt_required
    def put(self, qnId, ansId):
        userid_current = get_jwt_identity()
        current_user = userid_current['userId']
        db_obj = DBManager( app.config['DATABASE_URL'] )
        my_user_check_by_qn = db_obj.fetch_by_specific_param( 'userId', 'questions', 'userId', current_user )
        my_user_check_ans_auth = db_obj.fetch_by_specific_param( 'Ans_Auth_Id', 'answers', 'Ans_Auth_Id', current_user )
        if my_user_check_by_qn:
            db_obj.modify_ans_status(qnId, ansId)
            return {'message': 'Answer approved'}
        elif my_user_check_ans_auth:
            data = request.get_json()
            Answer = data['Answers']
            if not data:
                return {"message": 'Invalid, Your not allowed to change that.'}, 406
            if not isinstance( Answer, str ) or Answer.isspace() or Answer == "":
                return {"message": 'Invalid, Please enter a valid answer'}, 406
            else:
                db_obj.modify_ans( qnId, ansId, data )
                return {'message': 'Answer edited'}, 200

        return {"message": 'You not authorised to change the answer '}, 409

