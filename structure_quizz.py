import requests
import Utilitaires

class API_Call_to_send:
    api_key = Utilitaires.lecture_config("/config.json")['api_key']
    url_api = "https://quizapi.io/api/v1/questions"

    def __init__(self, tags: list, difficulty: str, category: str = None, limit: int = 10):
        self.tags = tags
        self.difficulty = difficulty
        self.category = category
        self.limit = limit

    def get_quizz(self):
        query = {
            "apiKey" : API_Call_to_send.api_key,
            "limit": self.limit,
            "category": self.category,
            "difficulty": self.difficulty,
            "tags": self.tags
        }
        response = requests.get(API_Call_to_send.url_api, params=query)
        return response
