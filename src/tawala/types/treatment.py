from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

from tawala.types.enums import RiskLevel, TreatmentPriority
from tawala.types.user import UserRead


class RiskTreatmentBase(BaseModel):
    treatment: str
    effectiveness: Optional[str] = None
    priority: Optional[TreatmentPriority] = None
    due_date: Optional[datetime] = None
    resources: Optional[str] = None
    monitoring: Optional[str] = None
    residual_risk: Optional[RiskLevel] = None
    performance_measures: Optional[str] = None
    owner_id: Optional[UUID] = None


class RiskTreatmentCreate(RiskTreatmentBase):
    risk_instance_id: UUID


class RiskTreatmentUpdate(RiskTreatmentBase):
    treatment: Optional[str] = None


class RiskTreatmentRead(RiskTreatmentBase):
    id: UUID
    risk_instance_id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None
    owner: Optional[UserRead] = None

    model_config = ConfigDict(from_attributes=True)
