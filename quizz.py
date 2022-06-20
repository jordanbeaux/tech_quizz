from question import Question
from reponse import Answer
import Utilitaires


class Quizz:
    """
    Structured quizz in the app. Get from the API and rebuild it from it. It's composed with the object Question.
    """
    def __init__(self, questions_list: list):
        if isinstance(questions_list, list):
            for elem in questions_list:
                if isinstance(elem, Question):
                    self.questions = questions_list
        else:
            self.questions = None
        self.score = 0

    def __check_response(self, user_response: Answer, quizz_response: list, question: Question):
        """
        Check if the player's answer is correct or not.

        :param user_response: Answer sent by the player
        :param quizz_response: Correct answer of the question
        :param question: The current question
        """
        point = []
        for reponse in quizz_response:
            if reponse in user_response.reponse_formatte:
                point.append(True)
            else:
                point.append(False)

        if False not in point:
            print("Well done, it's correct !")
            self.score += 1
            print(f'Your score is now : {self.score} points.')
        else:
            good_answer_to_display = question.format_answers_for_display()
            print("Incorrect. The right answer was :")
            for elem in good_answer_to_display:
                print(elem)

    @staticmethod
    def __format_good_answers(question: Question):
        """
        :param question: question to format.
        :return:
        """
        correct_answer_to_compare = []
        for answer, value in question.correct_answers.items():
            if value == 'true':
                correct_answer_to_compare.append(answer)
        return correct_answer_to_compare

    def deroulee_quizz(self):
        """
        Display the quizz and check the player's answers.
        """
        for question in self.questions:
            print(f'Question n° {self.questions.index(question) + 1} sur {len(self.questions)} :')
            print(f'{question.question}')
            print("Here are the options : ")
            compteur = 1
            for reponse in question.answers.values():
                if reponse is not None:
                    reponse_formatted = reponse
                    print("{compteur}) {reponse}".format(compteur=compteur, reponse=reponse_formatted))
                    if reponse is not None: compteur += 1
            print("There are several correct answers, pick them all" if question.multiple_answers == "true" else
                  "There is only one correct answer")

            reponse_to_compare = Quizz.__format_good_answers(question)
            while not question.valide_format_reponse:
                reponse_utilisateur_input = input("Type your  answers and sort them with comas : ")
                question.valide_format_reponse = Utilitaires.check_response_format(reponse_utilisateur_input)

            reponse_utilisateur_list = reponse_utilisateur_input.split(",")

            reponse_utilisateur = Answer(reponse_utilisateur_list)
            reponse_utilisateur.format_response(question.structure_reponse)

            self.__check_response(user_response=reponse_utilisateur, question=question,
                                  quizz_response=reponse_to_compare)

        print(f'The quizz is done. Your final score is {self.score} points.')
