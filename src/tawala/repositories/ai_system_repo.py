"""AI System repository module for managing AI systems.

Provides the AISystemRepository class for CRUD operations on AI systems.
"""
import json

from tawala.types.ai_system import AISystemCreate, AISystemRead, AISystemUpdate
from tawala.utils.http import HttpClient


class AISystemRepository:
    """Repository for managing AI systems in the Tawala platform.
    
    Provides methods for creating, retrieving, listing, and updating AI systems.
    
    Attributes:
        http: HTTP client for making API requests.
        logger: Optional logger for logging AISystemRepository operations.
    """
    
    def __init__(self, http: HttpClient, logger=None):
        """Initialize the AI System repository.
        
        Args:
            http: HTTP client instance for making requests.
            logger: Optional logger for logging AISystemRepository operations.
        """
        self.http = http
        self.logger = logger
        
    def __objectify(self, data: AISystemCreate | AISystemUpdate):
        """Convert Pydantic model to dictionary.
        
        Args:
            data: Pydantic model to convert.
            
        Returns:
            Dictionary representation of the model.
        """
        return json.loads(data.model_dump_json())

    def list(self) -> list[AISystemRead]:
        """Retrieve all AI systems.
        
        Returns:
            List of AISystemRead objects.
        """
        response = self.http.get("/ai-portfolio/systems")
        return [AISystemRead.model_validate(model) for model in response]

    def create(self, data: AISystemCreate) -> AISystemRead:
        """Create a new AI system.
        
        Args:
            data: AISystemCreate object with system details.
            
        Returns:
            AISystemRead object with the created system.
        """
        response = self.http.post("/ai-portfolio/systems", json=self.__objectify(data))
        return AISystemRead.model_validate(response)
    
    def get(self, id: str) -> AISystemRead:
        """Retrieve a specific AI system by ID.
        
        Args:
            id: The unique identifier of the system.
            
        Returns:
            AISystemRead object for the specified system.
        """
        response = self.http.get(f"/ai-portfolio/systems/{id}")
        return AISystemRead.model_validate(response)
    
    def update(self, id: str, data: AISystemUpdate) -> AISystemRead:
        """Update an existing AI system.
        
        Args:
            id: The unique identifier of the system to update.
            data: AISystemUpdate object with updated system details.
            
        Returns:
            AISystemRead object with the updated system.
        """
        response = self.http.put(f"/ai-portfolio/systems/{id}", json=self.__objectify(data))
        return AISystemRead.model_validate(response)