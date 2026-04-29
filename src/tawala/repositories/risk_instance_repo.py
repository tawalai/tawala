"""Risk Instance repository module for managing risk instances.

Provides the RiskInstanceRepository class for CRUD operations on risk instances.
"""
import json
from tawala.types.risk_instance import RiskInstanceCreate, RiskInstanceRead, RiskInstanceUpdate
from tawala.utils.http import HttpClient


class RiskInstanceRepository:
    """Repository for managing risk instances in the Tawala platform.
    
    Provides methods for creating, retrieving, listing, and updating risk instances.
    
    Attributes:
        http: HTTP client for making API requests.
        logger: Optional logger for logging RiskInstanceRepository operations.
    """
    
    def __init__(self, http: HttpClient, logger=None):
        """Initialize the Risk Instance repository.
        
        Args:
            http: HTTP client instance for making requests.
            logger: Optional logger for logging RiskInstanceRepository operations.
        """
        self.http = http
        self.logger = logger
        
    def __objectify(self, data: RiskInstanceCreate | RiskInstanceUpdate):
        """Convert Pydantic model to dictionary.
        
        Args:
            data: Pydantic model to convert.
            
        Returns:
            Dictionary representation of the model.
        """
        return json.loads(data.model_dump_json())

    def list(self) -> list[RiskInstanceRead]:
        """Retrieve all risk instances.
        
        Returns:
            List of RiskInstanceRead objects.
        """
        
        if self.logger:
            self.logger.debug("GET /risks/instances")
        
        response = self.http.get("/risks/instances")
        return [RiskInstanceRead.model_validate(model) for model in response]

    def create(self, data: RiskInstanceCreate) -> RiskInstanceRead:
        """Create a new risk instance.
        
        Args:
            data: RiskInstanceCreate object with risk instance details.
            
        Returns:
            RiskInstanceRead object with the created risk instance.
        """
        
        if self.logger:
            self.logger.debug("POST /risks/instances")
        
        response = self.http.post("/risks/instances", json=self.__objectify(data))
        return RiskInstanceRead.model_validate(response)
    
    def get(self, id: str) -> RiskInstanceRead:
        """Retrieve a specific risk instance by ID.
        
        Args:
            id: The unique identifier of the risk instance.
            
        Returns:
            RiskInstanceRead object for the specified risk instance.
        """
        
        if self.logger:
            self.logger.debug(f"GET /risks/instances/{id}")
        
        response = self.http.get(f"/risks/instances/{id}")
        return RiskInstanceRead.model_validate(response)
    
    def update(self, id: str, data: RiskInstanceUpdate) -> RiskInstanceRead:
        """Update an existing risk instance.
        
        Args:
            id: The unique identifier of the risk instance to update.
            data: RiskInstanceUpdate object with updated risk instance details.
            
        Returns:
            RiskInstanceRead object with the updated risk instance.
        """
        
        if self.logger:
            self.logger.debug(f"PUT /risks/instances/{id}")
        
        response = self.http.put(f"/risks/instances/{id}", json=data)
        return RiskInstanceRead.model_validate(response)