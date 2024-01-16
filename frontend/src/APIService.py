import os
import requests
from dotenv import load_dotenv

load_dotenv()

class APIService:
    instance = None

    def __init__(self):
        self.token = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = APIService()
        return cls.instance

    def init(self, token):
        self.token = token

    async def fetch(self, api_type):
        if 'API_ENDPOINT' not in os.environ:
            raise ValueError("Environment variable API_ENDPOINT not defined.")

        api_endpoint = os.environ['API_ENDPOINT']
        response = requests.get(f"{api_endpoint}{api_type}", headers={'token': self.token})
        
        response.raise_for_status()  # Raise an exception for bad responses (4xx, 5xx)
        
        return response.text
