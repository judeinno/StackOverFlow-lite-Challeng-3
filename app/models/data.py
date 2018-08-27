# my_questions is a list holds data that is taken by the class Questions
my_questions = []


def single_question(qn_id):
    """
    Helper Function:
    The function loops my_question and returns a
    question with a single id
    :param qn_id:
    :return: my_question
    """
    for my_question in my_questions:
        if my_question.qn_id == qn_id:
            return my_question
    return None