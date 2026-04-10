# client.py
from tawala.config import Config
from tawala.utils.http import HttpClient
from tawala.repositories.ai_model_repo import AIModelRepository

class TawalaClient:
    def __init__(self, api_key: str, base_url: str = "https://platformapi.tawala.ai"):
        self.config = Config(api_key=api_key, base_url=base_url)
        self.http = HttpClient(self.config)

        # resources
        self.models = AIModelRepository(self.http)