"""Configuration module for the Tawala SDK.

Defines configuration settings for connecting to the Tawala API.
"""
from pydantic import BaseModel

class Config(BaseModel):
    """Configuration settings for the Tawala API client.
    
    Attributes:
        api_key: API key for authentication with the Tawala platform.
        base_url: Base URL for the Tawala API endpoint.
        default_timeout: Default timeout for API requests in seconds.
    """
    api_key: str
    base_url: str
    default_timeout: int = 5