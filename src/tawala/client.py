# client.py
from tawala.config import Config
from tawala.repositories.ai_system_repo import AISystemRepository
from tawala.repositories.risk_instance_repo import RiskInstanceRepository
from tawala.repositories.risk_repo import RiskRepository
from tawala.utils.http import HttpClient
from tawala.repositories.ai_model_repo import AIModelRepository

class TawalaClient:
    def __init__(self, api_key: str, base_url: str = "https://platformapi.tawala.ai"):
        self.config = Config(api_key=api_key, base_url=base_url)
        self.http = HttpClient(self.config)

        # resources
        self.systems = AISystemRepository(self.http)
        self.models = AIModelRepository(self.http)
        self.risks = RiskRepository(self.http)
        self.risk_instances = RiskInstanceRepository(self.http)