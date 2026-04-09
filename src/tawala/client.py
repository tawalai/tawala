# client.py
from tawala.config import Config
from tawala.utils.http import HttpClient
from tawala.resources.models import ModelResource

class TawalaClient:
    def __init__(self, api_key: str, base_url: str = "https://api.tawala.ai"):
        self.config = Config(api_key=api_key, base_url=base_url)
        self.http = HttpClient(self.config)

        # resources
        self.models = ModelResource(self.http)