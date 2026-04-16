"""Risk type definitions for the Tawala SDK.

Defines Pydantic models for risk data.
"""
from pydantic import BaseModel

class Risk(BaseModel):
    """Schema for a risk.
    
    Attributes:
        id: Unique identifier for the risk.
        title: Title or name of the risk.
        description: Detailed description of the risk.
    """
    id: str
    title: str
    description: str