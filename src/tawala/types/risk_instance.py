"""Risk Instance type definitions for the Tawala SDK.

Defines Pydantic models for creating, updating, and reading risk instances.
"""
from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel

from tawala.types.enums import RiskLevel, RiskStatus
from tawala.types.review import RiskReviewRead
from tawala.types.treatment import RiskTreatmentRead
from tawala.types.user import User

class RiskInstanceBase(BaseModel):
    """Base risk instance model with common attributes.
    
    Attributes:
        likelihood: Likelihood level of the risk.
        impact: Impact level of the risk.
        residual: Residual risk level after treatment.
        status: Current status of the risk.
        board: Kanban board name for tracking.
        board_column: Column on the Kanban board.
        due_date: Due date for risk treatment.
        reviewed_at: When the risk was last reviewed.
    """
    likelihood: Optional[RiskLevel] = None
    impact: Optional[RiskLevel] = None
    residual: Optional[RiskLevel] = None
    status: Optional[RiskStatus] = None

    board: Optional[str] = None
    board_column: Optional[str] = None

    due_date: Optional[datetime] = None
    reviewed_at: Optional[datetime] = None

class RiskInstanceCreate(RiskInstanceBase):
    """Schema for creating a new risk instance.
    
    Attributes:
        likelihood: Likelihood level of the risk.
        impact: Impact level of the risk.
        residual: Residual risk level after treatment.
        status: Current status of the risk.
        board: Kanban board name for tracking.
        board_column: Column on the Kanban board.
        due_date: Due date for risk treatment.
        reviewed_at: When the risk was last reviewed.
        risk_id: ID of the associated risk.
        ai_system_id: ID of the associated AI system.
        owner_id: ID of the risk owner.
        collaborators: List of collaborator user IDs.
    """
    risk_id: UUID
    ai_system_id: UUID
    owner_id: UUID = None

    collaborators: Optional[List[UUID]] = None

class RiskInstanceUpdate(BaseModel):
    """Schema for updating an existing risk instance.
    
    All fields are optional to allow partial updates.
    
    Attributes:
        likelihood: Likelihood level of the risk.
        impact: Impact level of the risk.
        residual: Residual risk level after treatment.
        status: Current status of the risk.
        risk_id: ID of the associated risk.
        ai_system_id: ID of the associated AI system.
        board: Kanban board name for tracking.
        board_column: Column on the Kanban board.
        due_date: Due date for risk treatment.
        reviewed_at: When the risk was last reviewed.
        owner_id: ID of the risk owner.
        collaborators: List of collaborator user IDs.
        description: Description of the risk instance.
    """
    likelihood: Optional[RiskLevel] = None
    impact: Optional[RiskLevel] = None
    residual: Optional[RiskLevel] = None
    status: Optional[RiskStatus] = None
    
    risk_id: Optional[UUID] = None
    ai_system_id: Optional[UUID] = None

    board: Optional[str] = None
    board_column: Optional[str] = None

    due_date: Optional[datetime] = None
    reviewed_at: Optional[datetime] = None

    owner_id: Optional[UUID] = None
    collaborators: Optional[List[UUID]] = None
    description: Optional[str] = None

class RiskInstanceRead(RiskInstanceBase):
    """Schema for reading a risk instance from the API.
    
    Includes system-generated fields and related objects.
    
    Attributes:
        id: Unique identifier for the risk instance.
        likelihood: Likelihood level of the risk.
        impact: Impact level of the risk.
        residual: Residual risk level after treatment.
        status: Current status of the risk.
        risk_id: ID of the associated risk.
        ai_system_id: ID of the associated AI system.
        owner: Owner user details.
        created_at: Timestamp when the risk instance was created.
        updated_at: Timestamp when the risk instance was last updated.
        board: Kanban board name for tracking.
        board_column: Column on the Kanban board.
        collaborators: List of collaborator users.
        treatments: List of risk treatments associated with this instance.
        reviews: List of risk reviews associated with this instance.
        description: Description of the risk instance.
    """
    id: UUID

    risk_id: UUID
    ai_system_id: UUID
    owner: Optional[User] = None

    created_at: datetime
    updated_at: Optional[datetime] = None

    collaborators: Optional[List[User]] = None
    treatments: Optional[List[RiskTreatmentRead]] = None
    reviews: Optional[List[RiskReviewRead]] = None
    description: Optional[str] = None
