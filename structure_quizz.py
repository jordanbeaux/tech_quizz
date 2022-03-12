from distutils.command.config import config
import requests
import Utilitaires

class API_Call_to_send:
    config_file = Utilitaires.lecture_config("./config.json")
    api_key = config_file['api_key']
    url_api = "https://quizapi.io/api/v1/questions"

    def __init__(self, difficulty: str, category: str = None, limit: int = 10, tags: list =None):
        self.tags = tags
        self.difficulty = difficulty
        self.category = category
        self.limit = limit

    def get_quizz(self):
        query = {
            
            "limit": self.limit,
            "category": self.category,
            "difficulty": self.difficulty,
            "tags": self.tags
        }
        response = requests.post(API_Call_to_send.url_api, params=query, headers={'X-Api-Key':API_Call_to_send.api_key})
        return response
