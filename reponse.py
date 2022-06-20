class Answer:
    """
    Answers to the quiz's question.
    """
    transco_reponse = ['a', 'b', 'c', 'd', 'e', 'f']

    def __init__(self, reponse: list):
        self.reponse = reponse
        self.reponse_formatte = None

    def format_response(self, structure_reponse: str):
        """
        Format the answer to display them to the player.
        :param structure_reponse:
        """
        reponse_formatte = []
        for elem in self.reponse:
            if int(elem) in range(1, 6):
                reponse_formatte.append(structure_reponse.format(val=Answer.transco_reponse[int(elem) - 1]))
        self.reponse_formatte = reponse_formatte
