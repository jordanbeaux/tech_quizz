import json
import logging


def lecture_config(file_to_open: str) -> dict:
    """
    Open and read the content of a file from its absolute path.

    :param file_to_open: file's path to open
    :return: file opened and loaded
    """
    try:
        with open(file_to_open, mode='r', encoding='utf-8') as file:
            config = json.load(file)
        return config
    except:
        logging.exception("Error while getting the conf file (file : {})".format(file_to_open))


def verif_reponse_format(list_reponse):
    for elem in list_reponse:
        if not elem.isdigit() or int(elem) > 6 or int(elem) < 0:
            print("One of your answers isn't in a valid format. Type them again")
            return False
        else:
            return True
