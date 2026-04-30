"""HTTP client module for making requests to the Tawala API.

Provides the HttpClient class which handles authentication and API communication.
"""
import requests

from tawala.utils.config import Config
from tawala.utils.exceptions import TawalaAPIError, TawalaAuthenticationError, TawalaTimeoutError
from urllib3.util.retry import Retry

class HttpClient:
    """HTTP client for making authenticated requests to the Tawala API.
    
    Handles request headers, error handling, and JSON serialization/deserialization.
    
    Attributes:
        base_url: Base URL for all API requests.
        api_key: API key for authentication.
        session: Session object for making requests.
        timeout: Request timeout in seconds.
        logger: Optional logger for logging HTTP requests and responses.
    """
    
    def __init__(self, config: Config, logger=None):
        """Initialize the HTTP client.
        
        Args:
            config: Configuration object containing base_url and api_key.
        """
        self.base_url = config.base_url
        self.api_key = config.api_key
        self.session = requests.Session()
        self.timeout = config.default_timeout
        self.logger = logger
        
        retry_strategy = Retry(
            total=3,  # max retries
            backoff_factor=0.5,  # exponential backoff
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST"],
        )
        
        adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
        self.session.mount(self.base_url, adapter)

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
        
        try:
            response = self.session.get(
                self.base_url + path,
                headers=self._headers(),
                timeout=self.timeout,
                params=params
            )
        except requests.exceptions.Timeout as exc:
            raise TawalaTimeoutError(f"GET {self.base_url + path} request timed out") from exc
        except requests.exceptions.ConnectionError as exc:
            raise TawalaAPIError(f"GET {self.base_url + path} request failed: {exc}") from exc

        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            
            if response.status_code == 401:
                raise TawalaAuthenticationError(
                    f"Authentication failed: {response.text}", 
                    status_code=response.status_code
                ) from exc
            else:
                raise TawalaAPIError(
                    f"GET API {response.url} request failed with status {response.status_code}: {response.text}",
                    status_code=response.status_code
                ) from exc

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
        
        try:
            response = self.session.post(
                self.base_url + path,
                headers=self._headers(),
                timeout=self.timeout,
                json=json
            )
        except requests.exceptions.Timeout as exc:
            raise TawalaTimeoutError(f"POST {self.base_url + path} request timed out") from exc
        except requests.exceptions.ConnectionError as exc:
            raise TawalaAPIError(f"GET {self.base_url + path} request failed: {exc}") from exc
        
        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            
            if response.status_code == 401:
                raise TawalaAuthenticationError(
                    f"Authentication failed: {response.text}", 
                    status_code=response.status_code
                ) from exc
            else:
                raise TawalaAPIError(
                    f"POST API {response.url} request failed with status {response.status_code}: {response.text}", 
                    status_code=response.status_code
                ) from exc

        try:
            return response.json()
        except ValueError as exc:
            raise ValueError(f"POST {response.url} returned invalid JSON: {exc}") from exc