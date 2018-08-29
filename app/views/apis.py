from flask import Blueprint
from flask_restful import Api
from app.views.questions_view import QuestionManager, SingleQuestionManager, DeleteQuestionManager
from app.views.answer_view import AnswerManager, UpdateAnswer

# Initialistion of blueprint, giving it a name and a url prefix
blue_print = Blueprint('Qns_Bp', __name__, url_prefix='/api/v1')

# Making the blueprint an instance of the class Api
api = Api(blue_print)

api.add_resource(QuestionManager, '/questions')

api.add_resource(SingleQuestionManager, '/questions/<int:qnId>')

api.add_resource(DeleteQuestionManager, '/questions/<int:qnId>')

api.add_resource(AnswerManager, '/questions/<int:qnId>/answers')

api.add_resource(UpdateAnswer, '/questions/<int:qnId>/answers/<int:ansId>')