from question import Question
from reponse import Reponse


class Quizz:
    def __init__(self, liste_questions: list):
        self.questions = liste_questions if isinstance(liste_questions, Question) else None
        self.score = 0

    def __check_response(self, reponse: Reponse):

