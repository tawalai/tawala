from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel

from tawala.types.enums import RiskLevel, RiskStatus

class RiskInstance(BaseModel):
    risk_id: UUID
    ai_system_id: UUID
    likelihood: Optional[RiskLevel] = None
    impact: Optional[RiskLevel] = None
    residual: Optional[RiskLevel] = None
    status: Optional[RiskStatus] = None
    due_date: Optional[datetime] = None
    reviewed_at: Optional[datetime] = None
    