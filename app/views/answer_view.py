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
        if db_obj.fetch_question_values( qnId, current_user ):
            return {'message': 'Yor can not answer your own question'}
        else:
            db_obj.fetch_question_value(qnId)
            db_obj.create_answer(qnId, current_user, data)
            return {'message': 'answer successfully created'}



