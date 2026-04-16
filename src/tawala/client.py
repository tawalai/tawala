"""Main client module for the Tawala AI Risk Management SDK.

Provides the TawalaClient class which serves as the main entry point for interacting
with the Tawala platform API.
"""
from tawala.config import Config
from tawala.repositories.ai_system_repo import AISystemRepository
from tawala.repositories.risk_instance_repo import RiskInstanceRepository
from tawala.repositories.risk_repo import RiskRepository
from tawala.utils.http import HttpClient
from tawala.repositories.ai_model_repo import AIModelRepository

class TawalaClient:
    """Main client for interacting with the Tawala AI Risk Management platform.
    
    Provides access to repositories for managing AI systems, models, risks, and risk instances.
    
    Attributes:
        config: Configuration object containing API key and base URL.
        http: HTTP client for making API requests.
        systems: Repository for managing AI systems.
        models: Repository for managing AI models.
        risks: Repository for managing risks.
        risk_instances: Repository for managing risk instances.
    """
    
    def __init__(self, api_key: str, base_url: str = "https://platformapi.tawala.ai"):
        """Initialize the Tawala client.
        
        Args:
            api_key: API key for authentication with the Tawala platform.
            base_url: Base URL for the Tawala API (defaults to production URL).
        """
        self.config = Config(api_key=api_key, base_url=base_url)
        self.http = HttpClient(self.config)

        # resources
        self.systems = AISystemRepository(self.http)
        self.models = AIModelRepository(self.http)
        self.risks = RiskRepository(self.http)
        self.risk_instances = RiskInstanceRepository(self.http)