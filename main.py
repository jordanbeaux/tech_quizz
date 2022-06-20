from structure_quizz import API_Call_to_send
from display_quizz import display_quizz

Quizz_test_init = API_Call_to_send(difficulty="easy", category="Docker", limit=2)

display_quizz(quizz_get=Quizz_test_init)
