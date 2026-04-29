"""AI Model repository module for managing AI models.

Provides the AIModelRepository class for CRUD operations on AI models.
"""
import json

from tawala.types.ai_model import AIModelCreate, AIModelRead, AIModelUpdate
from tawala.utils.http import HttpClient


class AIModelRepository:
    """Repository for managing AI models in the Tawala platform.
    
    Provides methods for creating, retrieving, listing, and updating AI models.
    
    Attributes:
        http: HTTP client for making API requests.
        logger: Optional logger for logging AIModelRepository operations.
    """
    
    def __init__(self, http: HttpClient, logger=None):
        """Initialize the AI Model repository.
        
        Args:
            http: HTTP client instance for making requests.
            logger: Optional logger for logging AIModelRepository operations.
        """
        self.http = http
        self.logger = logger
        
    def __objectify(self, data: AIModelCreate | AIModelUpdate):
        """Convert Pydantic model to dictionary.
        
        Args:
            data: Pydantic model to convert.
            
        Returns:
            Dictionary representation of the model.
        """
        return json.loads(data.model_dump_json())

    def list(self) -> list[AIModelRead]:
        """Retrieve all AI models.
        
        Returns:
            List of AIModelRead objects.
        """
        response = self.http.get("/ai-portfolio/models")
        return [AIModelRead.model_validate(model) for model in response]

    def create(self, data: AIModelCreate) -> AIModelRead:
        """Create a new AI model.
        
        Args:
            data: AIModelCreate object with model details.
            
        Returns:
            AIModelRead object with the created model.
        """
        response = self.http.post("/ai-portfolio/models", json=self.__objectify(data))
        return AIModelRead.model_validate(response)
    
    def get(self, id: str) -> AIModelRead:
        """Retrieve a specific AI model by ID.
        
        Args:
            id: The unique identifier of the model.
            
        Returns:
            AIModelRead object for the specified model.
        """
        response = self.http.get(f"/ai-portfolio/models/{id}")
        return AIModelRead.model_validate(response)
    
    def update(self, id: str, data: AIModelUpdate) -> AIModelRead:
        """Update an existing AI model.
        
        Args:
            id: The unique identifier of the model to update.
            data: AIModelUpdate object with updated model details.
            
        Returns:
            AIModelRead object with the updated model.
        """
        response = self.http.put(f"/ai-portfolio/models/{id}", json=self.__objectify(data))
        return AIModelRead.model_validate(response)