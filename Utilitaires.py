import json
import logging


def lecture_config(file_to_open: str) -> dict:
    """
    Sert à ouvrir et lire le contenu d'un fichier à partir du chemin absolu de celui ci.

    :param file_to_open: chemin du fichier de config à ouvrir
    :return: fichier ouvert et chargé
    """
    try:
        with open(file_to_open, mode='r', encoding='utf-8') as file:
            config = json.load(file)
        return config
    except:
        logging.exception("Erreur lors de la récupération des fichiers de configurations (fichiers : {})"
                          .format(file_to_open))


def verif_reponse_format(list_reponse: list):
    for elem in list_reponse:
        if not elem.isdigit() or int(elem) > 6 or int(elem) < 0:
            print("Une de vos réponses n'est pas dans un format valide. Veuillez les re saisir")
            return False
        else:
            return True
