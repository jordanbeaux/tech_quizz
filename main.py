from structure_quizz import API_Call_to_send
from question import Question
from quizz import Quizz



Quizz_test_init = API_Call_to_send(difficulty="easy", category="Docker", limit=2)
Test_quizz = Quizz_test_init.get_quizz()
Quizz_get = Test_quizz.json()

New_Quizz = []
for question in Quizz_get:
    new_question = Question(id_question=question['id'],
    question=question['question'], description=question['description'], multiple_answers=question['multiple_correct_answers'],
        explanation=question['explanation'],
    tip=question['tip'], tags=question['tags'], category=question['category'], 
    difficulty=question['difficulty'], answers=question['answers'], correct_answers=question['correct_answers'])
    New_Quizz.append(new_question)

created_quizz = Quizz(New_Quizz)

created_quizz.deroulee_quizz()