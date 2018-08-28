
"""This module handles database queries"""


class User:
    """This class does all database related stuff for the user"""

    def __init__(self, userId, email, username, password):
        self.user_id = userId
        self.email = email
        self.username = username
        self.password = password

class Questions(object):
    """
    The class is a model that:
    Initialises the app variables
    Converts the app variables to json data
    """

    def __init__(self, qnId, Question):
        """
        Class initialisation method
        :param qn_id:
        :param question:
        """

        self.qnId = qnId
        self.Question = Question

class Answers(object):
    """
    The class is a model that:
    Initialises the app variables
    Converts the app variables to json data
    """

    def __init__(self, ansId, Answer):
        """
        Class initialisation method
        :param ansid:
        :param Answer:
        """

        self.qnId = ansId
        self.Question = Answer



