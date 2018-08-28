
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

    def to_json(self):
        """
        Method converts data to json data
        :return: json_data
        """
        json_data = {
            'qnId': self.qnId,
            'Question': self.Question,
        }
        return json_data


