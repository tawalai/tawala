"""Authentication management module for the Tawala SDK.

Handles API key exchange and token management.
"""

class AuthManager:
    """Manages authentication and token exchange with the Tawala API.
    
    Attributes:
        http: HTTP client for making authentication requests.
        token: Current access token for authenticated requests.
    """
    
    def __init__(self, http):
        """Initialize the AuthManager.
        
        Args:
            http: HTTP client instance for making requests.
        """
        self.http = http
        self.token = None

    def authenticate(self, api_key):
        """Exchange an API key for an access token.
        
        Args:
            api_key: The API key to exchange for a token.
        """
        res = self.http.post("/auth/exchange", json={"api_key": api_key})
        self.token = res["access_token"]