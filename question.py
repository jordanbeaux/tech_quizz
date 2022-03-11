class Question:
    def __init__(self, id_question: int, question: str, description: str, multiple_answers: bool, explanation: str, tip: str, tags: list,
                 category: str, difficulty: str, answers: dict, correct_answers: dict):
        self.id = id_question
        self.question = question
        self.description = description
        self.multiple_answers = multiple_answers
        self.explanation = explanation
        self.tip = tip
        self.tags = tags
        self.category = category
        self.difficulty = difficulty
        self.answers = answers
        self.correct_answers = correct_answers