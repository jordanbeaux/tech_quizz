from question import Question
from reponse import Reponse


class Quizz:
    def __init__(self, liste_questions: list):
        if isinstance(liste_questions, list):
            for elem in liste_questions:
                if isinstance(elem, Question):
                    self.questions = liste_questions
        else:
            self.questions = None
        self.score = 0

    def __check_response(self, reponse: Reponse, question: Question):
        if reponse == question.correct_answers:
            print("Bravo c'est la bonne réponse !")
            self.score += 1
            print(f'Votre score est désormais de : {self.score} points.')
        else:
            print(f"Ce n'est pas la bonne réponse. La bonne réponse était : {question.correct_answers}")

    def deroulee_quizz(self):
        for question in self.questions:
            print(f'Question n° {self.questions.index(question)+1} sur {len(self.questions)} :')
            print(f'{question.question}')
            print("Voici les propositions : ")
            for reponse in question.answers.values():
                print(reponse if reponse is not None else "")
            print("Il y a plusieurs bonnes réponses" if question.multiple_answers else "Il n'y a qu'une bonne réponse")

            reponse_utilisateur = input("Entrez vos réponses, séparer par des virgules : ")

            Quizz.__check_response(reponse=reponse_utilisateur, question=question)

        print(f'Le quizz est terminée. Votre score final est de {self.score}')