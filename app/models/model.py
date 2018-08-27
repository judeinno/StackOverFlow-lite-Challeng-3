
class Questions(object):
    """
    The class is a model that:
    Initialises the app variables
    Converts the app variables to json data
    """

    def __init__(self, qn_id, question):
        """
        Class initialisation method
        :param qn_id:
        :param question:
        :param answer:
        """
        self.qn_id = qn_id
        self.question = question
        self.answer = []

    def to_json(self):
        """
        Method converts data to json data
        :return: json_data
        """
        json_data = {
            'qn_id': self.qn_id,
            'question': self.question,
            'answer': self.answer
        }
        return json_data


