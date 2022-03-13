class Reponse:
    transco_reponse = ['a', 'b', 'c', 'd', 'e', 'f']
    def __init__(self, reponse: list):
        self.reponse = reponse
        self.reponse_formatte = None

    def format_reponse(self, structure_reponse: str):
        reponse_formatte = []
        for elem in self.reponse:
            if int(elem) in range(1, 6):
                reponse_formatte.append(structure_reponse.format(val=Reponse.transco_reponse[int(elem)-1]))
        self.reponse_formatte = reponse_formatte







