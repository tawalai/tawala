from typing import List, Optional
from pydantic import BaseModel, Field
from uuid import UUID

from tawala.types.ai_model import AIModelRead
from tawala.types.user import UserRead

class AISystemCreate(BaseModel):
    name: str
    description: Optional[str] = None

    intended_purpose: str
    decision_type: Optional[str] = Field(None, description="assistive | automated | autonomous")

    business_owner: Optional[UUID] = None 
    technical_owner: Optional[UUID] = None

    organization_unit: Optional[str] = None
    lifecycle_status: str = Field(None, description="idea | development | testing | deployed | retired")

    eu_ai_act_risk_class: Optional[str] = Field(None, description="minimal | limited | high | prohibited")
    human_oversight_description: Optional[str] = None
    
    models: Optional[List[UUID]] 


class AISystemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    intended_purpose: Optional[str] = None
    decision_type: Optional[str] = None

    business_owner: Optional[UUID] = None
    technical_owner: Optional[UUID] = None

    organization_unit: Optional[str] = None
    lifecycle_status: Optional[str] = None
    eu_ai_act_risk_class: Optional[str] = None
    human_oversight_description: Optional[str] = None
    
    models: Optional[List[UUID]] 


class AISystemRead(BaseModel):
    id: UUID
    name: str
    description: Optional[str]

    intended_purpose: str
    decision_type: Optional[str]

    business_owner: Optional[UserRead]
    technical_owner: Optional[UserRead]

    organization_unit: Optional[str]
    lifecycle_status: Optional[str]
    eu_ai_act_risk_class: Optional[str]

    human_oversight_description: Optional[str]
    
    models: Optional[List[AIModelRead]] 


