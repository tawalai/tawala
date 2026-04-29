"""Risk repository module for managing risks.

Provides the RiskRepository class for CRUD operations on risks.
"""
from tawala.types.risk import Risk
from tawala.utils.http import HttpClient


class RiskRepository:
    """Repository for managing risks in the Tawala platform.
    
    Provides methods for creating, retrieving, listing, and updating risks.
    
    Attributes:
        http: HTTP client for making API requests.
        logger: Optional logger for logging RiskRepository operations.
    """
    
    def __init__(self, http: HttpClient, logger=None):
        """Initialize the Risk repository.
        
        Args:
            http: HTTP client instance for making requests.
            logger: Optional logger for logging RiskRepository operations.
        """
        self.http = http
        self.logger = logger

    def list(self) -> list[Risk]:
        """Retrieve all risks.
        
        Returns:
            List of Risk objects.
        """
        response = self.http.get("/risks")
        return [Risk.model_validate(model) for model in response]

    def create(self, data: Risk) -> Risk:
        """Create a new risk.
        
        Args:
            data: Risk object with risk details.
            
        Returns:
            Risk object with the created risk.
        """
        response = self.http.post("/risks", json=data)
        return Risk.model_validate(response)
    
    def get(self, id: str) -> Risk:
        """Retrieve a specific risk by ID.
        
        Args:
            id: The unique identifier of the risk.
            
        Returns:
            Risk object for the specified risk.
        """
        response = self.http.get(f"/risks/{id}")
        return Risk.model_validate(response)
    
    def update(self, id: str, data) -> Risk:
        """Update an existing risk.
        
        Args:
            id: The unique identifier of the risk to update.
            data: Risk object with updated risk details.
            
        Returns:
            Risk object with the updated risk.
        """
        response = self.http.put(f"/risks/{id}", json=data)
        return Risk.model_validate(response)