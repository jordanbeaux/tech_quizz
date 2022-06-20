import logging

from structure_quizz import API_Call_to_send
from question import Question
from quizz import Quizz


def display_quizz(quizz_get: API_Call_to_send) -> None:
    """
    Generate a quizz from the API. It uses the structure of the custom code to display it and play with it.

    param quizz_get: Quizz get from the API
    """
    test_quizz = quizz_get.get_quizz()
    quizz_get = test_quizz.json()

    new_quizz = []
    try:
        for question in quizz_get:
            new_question = Question(id_question=question['id'],
                                    question=question['question'], description=question['description'],
                                    multiple_answers=question['multiple_correct_answers'],
                                    explanation=question['explanation'],
                                    tip=question['tip'], tags=question['tags'], category=question['category'],
                                    difficulty=question['difficulty'], answers=question['answers'],
                                    correct_answers=question['correct_answers'])
            new_quizz.append(new_question)

        created_quizz = Quizz(new_quizz)

        created_quizz.deroulee_quizz()

    except TypeError:
        logging.ERROR("You need to enter your API key in the config.json file")
