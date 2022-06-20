import requests
import Utilitaires


class API_Call_to_send:
    """
    API call.
    """
    config_file = Utilitaires.read_config("./config.json")
    api_key = config_file['api_key']
    url_api = "https://quizapi.io/api/v1/questions"

    def __init__(self, difficulty: str, category: str = None, limit: int = 10, tags: list = None):
        self.tags = tags
        self.difficulty = difficulty
        self.category = category
        self.limit = limit

    def get_quizz(self):
        """
        Get the quizz from the API.
        The 'user-agent' is necessary to make the API's call but you can use what you want.
        """
        query = {
            "limit": self.limit,
            "category": self.category,
            "difficulty": self.difficulty,
            "tags": self.tags
        }
        headers = {'x-api-key': API_Call_to_send.api_key, 'user-agent': 'batman'}
        response = requests.get(url=API_Call_to_send.url_api, params=query, headers=headers)
        return response
