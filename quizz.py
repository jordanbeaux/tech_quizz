from question import Question
from reponse import Reponse
import Utilitaires


class Quizz:
    def __init__(self, liste_questions: list):
        if isinstance(liste_questions, list):
            for elem in liste_questions:
                if isinstance(elem, Question):
                    self.questions = liste_questions
        else:
            self.questions = None
        self.score = 0

    def __check_response(self, reponse_utilisateur: Reponse, reponse_quizz: list, question: Question):
        point_accorde = []
        for reponse in reponse_quizz:
            if reponse in reponse_utilisateur.reponse_formatte:
                point_accorde.append(True)
            else:
                point_accorde.append(False)

        if False not in point_accorde:
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
        correct_answer_to_compare = []
        for answer, value in question.correct_answers.items():
            if value == 'true':
                correct_answer_to_compare.append(answer)
        return correct_answer_to_compare

    def deroulee_quizz(self):
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
                question.valide_format_reponse = Utilitaires.verif_reponse_format(reponse_utilisateur_input)

            reponse_utilisateur_list = reponse_utilisateur_input.split(",")

            reponse_utilisateur = Reponse(reponse_utilisateur_list)
            reponse_utilisateur.format_reponse(question.structure_reponse)

            self.__check_response(reponse_utilisateur=reponse_utilisateur, question=question,
                                  reponse_quizz=reponse_to_compare)

        print(f'The quizz is done. Your final score is {self.score} points.')
