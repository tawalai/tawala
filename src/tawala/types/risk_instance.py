from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel

from tawala.types.enums import RiskLevel, RiskStatus
from tawala.types.review import RiskReviewRead
from tawala.types.treatment import RiskTreatmentRead
from tawala.types.user import UserRead

class RiskInstanceBase(BaseModel):
    likelihood: Optional[RiskLevel] = None
    impact: Optional[RiskLevel] = None
    residual: Optional[RiskLevel] = None
    status: Optional[RiskStatus] = None

    board: Optional[str] = None
    board_column: Optional[str] = None

    due_date: Optional[datetime] = None
    reviewed_at: Optional[datetime] = None

class RiskInstanceCreate(RiskInstanceBase):
    risk_id: UUID
    ai_system_id: UUID
    owner_id: UUID = None

    collaborators: Optional[List[UUID]] = None

class RiskInstanceUpdate(BaseModel):
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
    id: UUID

    risk_id: UUID
    ai_system_id: UUID
    owner: Optional[UserRead] = None

    created_at: datetime
    updated_at: Optional[datetime] = None

    collaborators: Optional[List[UserRead]] = None
    treatments: Optional[List[RiskTreatmentRead]] = None
    reviews: Optional[List[RiskReviewRead]] = None
    description: Optional[str] = None
