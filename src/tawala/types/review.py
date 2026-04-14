from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

from tawala.types.user import UserRead


class RiskReviewBase(BaseModel):
    findings: Optional[str] = None
    recommendations: Optional[str] = None
    reviewer_id: UUID

class RiskReviewCreate(RiskReviewBase):
    risk_instance_id: UUID

class RiskReviewUpdate(RiskReviewBase):
    reviewed_at: datetime

class RiskReviewRead(RiskReviewBase):
    id: UUID
    risk_instance_id: UUID
    reviewer: Optional[UserRead] = None
    created_at: datetime
    reviewed_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
