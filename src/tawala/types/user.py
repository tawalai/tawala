"""User type definitions for the Tawala SDK.

Defines Pydantic models for user data management.
"""
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class User(BaseModel):
    """User model representing a user in the Tawala platform.
    
    Attributes:
        id: Unique identifier for the user.
        email: User's email address.
        created_at: Timestamp when the user account was created.
        name: User's display name.
        role: User's role in the system.
    """
    id: UUID
    email: str
    created_at: datetime
    name: Optional[str]
    role: Optional[str]