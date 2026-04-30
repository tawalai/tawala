"""Custom exceptions for the Tawala SDK."""

class TawalaException(Exception):
    """Base exception for all Tawala SDK errors."""
    pass

class TawalaAPIError(TawalaException):
    """Exception raised for API-related errors."""
    
    def __init__(self, message: str, status_code: int = None, response_data: dict = None):
        super().__init__(message)
        self.status_code = status_code
        self.response_data = response_data

class TawalaAuthenticationError(TawalaAPIError):
    """Exception raised for authentication failures."""
    pass

class TawalaValidationError(TawalaException):
    """Exception raised for data validation errors."""
    pass

class TawalaConfigurationError(TawalaException):
    """Exception raised for configuration-related errors."""
    pass

class TawalaPolicyError(TawalaException):
    """Exception raised for policy evaluation errors."""
    pass