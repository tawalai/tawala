"""HTTP client module for making requests to the Tawala API.

Provides the HttpClient class which handles authentication and API communication.
"""
import requests

from tawala.utils.config import Config

class HttpClient:
    """HTTP client for making authenticated requests to the Tawala API.
    
    Handles request headers, error handling, and JSON serialization/deserialization.
    
    Attributes:
        base_url: Base URL for all API requests.
        api_key: API key for authentication.
        logger: Optional logger for logging HTTP requests and responses.
    """
    
    def __init__(self, config: Config, logger=None):
        """Initialize the HTTP client.
        
        Args:
            config: Configuration object containing base_url and api_key.
        """
        self.base_url = config.base_url
        self.api_key = config.api_key
        self.logger = logger

    def _headers(self):
        """Generate HTTP headers for API requests.
        
        Returns:
            Dictionary containing Authorization and Content-Type headers.
        """
        return {
            "Authorization": f"ApiKey {self.api_key}",
            "Content-Type": "application/json"
        }

    def get(self, path, params=None):
        """Make a GET request to the API.
        
        Args:
            path: API endpoint path.
            params: Optional query parameters.
            
        Returns:
            JSON response from the API.
            
        Raises:
            requests.HTTPError: If the HTTP request fails.
            ValueError: If the response is not valid JSON.
        """
        
        if self.logger:
            self.logger.debug(f"GET {self.base_url + path}")
        
        response = requests.get(self.base_url + path, headers=self._headers(), params=params)
        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            raise requests.HTTPError(
                f"GET {response.url} failed with status {response.status_code}: {response.text}") from exc

        try:
            return response.json()
        except ValueError as exc:
            raise ValueError(f"GET {response.url} returned invalid JSON: {exc}") from exc

    def post(self, path, json=None):
        """Make a POST request to the API.
        
        Args:
            path: API endpoint path.
            json: Optional JSON body for the request.
            
        Returns:
            JSON response from the API.
            
        Raises:
            requests.HTTPError: If the HTTP request fails.
            ValueError: If the response is not valid JSON.
        """
        
        if self.logger:
            self.logger.debug(f"POST {self.base_url + path}")
        
        response = requests.post(self.base_url + path, headers=self._headers(), json=json)
        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            raise requests.HTTPError(
                f"POST {response.url} failed with status {response.status_code}: {response.text}") from exc

        try:
            return response.json()
        except ValueError as exc:
            raise ValueError(f"POST {response.url} returned invalid JSON: {exc}") from exc