"""Main client module for the Tawala AI Risk Management SDK.

Provides the TawalaClient class which serves as the main entry point for interacting
with the Tawala platform API.
"""
import logging
from tawala.config import Config
from tawala.repositories.ai_system_repo import AISystemRepository
from tawala.repositories.risk_instance_repo import RiskInstanceRepository
from tawala.repositories.risk_repo import RiskRepository
from tawala.utils.http import HttpClient
from tawala.repositories.ai_model_repo import AIModelRepository
from tawala.utils.tawala_logger import TawalaLogger

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
    
    def __init__(self, api_key: str, base_url: str = "https://platformapi.tawala.ai", debug: bool = False):
        """Initialize the Tawala client.
        
        Args:
            api_key: API key for authentication with the Tawala platform.
            base_url: Base URL for the Tawala API (defaults to production URL).
            debug: Enable debug mode (defaults to False).
        """
        
        self.logger = TawalaLogger(name="tawala.client").get_logger()
        
        if debug:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
        
        
        self.config = Config(api_key=api_key, base_url=base_url)
        self.http = HttpClient(self.config, logger=self.logger)

        # resources
        self.systems = AISystemRepository(self.http, logger=self.logger)
        self.models = AIModelRepository(self.http, logger=self.logger)
        self.risks = RiskRepository(self.http, logger=self.logger)
        self.risk_instances = RiskInstanceRepository(self.http, logger=self.logger)