# from flask_restful import Resource
# from app.models.data import my_questions
# from flask import request
# from app.models.model import Questions
# from app.models.data import single_question
#
#
# class QuestionManager(Resource):
#     """
#     Class holds the end points to:
#     Get all the user questions
#     Post a new question to the list my_questions
#     """
#     def get(self):
#         """
#                 The get method initisalises an empty list
#                 Then it appends the questions in my questions to the list reply
#                 which is a list of all questions
#                 :return: reply
#                 """
#         reply = []
#         for my_question in my_questions:
#             reply.append(my_question.to_json())
#         return reply
#
#
#     def post(self):
#         """
#         The post method:
#         It gets the length of the list my_questions increments it by 1
#         gets the method get_json from requests stores it in data
#         Then uses the method to convert Question and answer to json data
#         and then appends the question and empty answer list the its id
#         :return: {'message': 'Question Added successfully'}, 201
#         """
#         data = request.get_json()
#         qn_id = len(my_questions) + 1
#         question = data['question']
#         if not isinstance(question, str) or question.isspace() or question == "":
#             return {"message": 'Invalid, Please make sure your asking the question well'}, 406
#         else:
#             my_questions.append( Questions(qn_id,question))
#             return {'message': 'Question Added successfully'}, 201
#
#
# class SingleQuestionManager(Resource):
#     """
#        Class holds the end points to:
#        Get a single user question
#     """
#
#     def get(self, qn_id):
#         """
#            The get method initisalises an empty list
#            uses the imported helper function that returns a single question
#            Then it appends a question with provided question_id in the url to reply
#            :return: reply
#         """
#         reply = []
#         one_question = single_question(qn_id)
#         if one_question is None:
#             return {"message": 'Question not found'}, 404
#         else:
#             reply.append( one_question.to_json() )
#             return reply
#
#
#
#
# class AnswerManager(Resource):
#     """
#        Class holds the end points to:
#        Post an answer to a given question
#     """
#
#     def post(self, qn_id):
#         """
#             The post method:
#             Uses the imported helper function to get a single question in the my_questions list
#             Then uses the function get_json in requests to convert the provided answer to json data
#             After which it append the answer to the Answer list in Questions
#             :return: {'message': 'Answer Added successfully'}, 201
#         """
#         one_question = single_question(qn_id)
#         data = request.get_json()
#         answer = data['answer']
#         if not isinstance(answer, str) or answer.isspace() or answer == "":
#             return {"message": 'Invalid, Please make sure you posted the answer well'}, 406
#         else:
#             one_question.answer.append(answer)
#             return {"message": 'Answer successfully added'}, 201
#
