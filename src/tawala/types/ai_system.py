"""AI System type definitions for the Tawala SDK.

Defines Pydantic models for creating, updating, and reading AI systems.
"""
from typing import List, Optional
from pydantic import BaseModel, Field
from uuid import UUID

from tawala.types.ai_model import AIModelRead
from tawala.types.user import User

class AISystemCreate(BaseModel):
    """Schema for creating a new AI system.
    
    Attributes:
        name: Name of the AI system.
        description: Description of the AI system.
        intended_purpose: Intended purpose of the system.
        decision_type: Type of decision (assistive | automated | autonomous).
        business_owner: ID of the business owner.
        technical_owner: ID of the technical owner.
        organization_unit: Associated organizational unit.
        lifecycle_status: Current lifecycle status (idea | development | testing | deployed | retired).
        eu_ai_act_risk_class: EU AI Act risk class (minimal | limited | high | prohibited).
        human_oversight_description: Description of human oversight measures.
        models: List of AI model IDs used by this system.
    """
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
    """Schema for updating an existing AI system.
    
    All fields are optional to allow partial updates.
    
    Attributes:
        name: Name of the AI system.
        description: Description of the AI system.
        intended_purpose: Intended purpose of the system.
        decision_type: Type of decision (assistive | automated | autonomous).
        business_owner: ID of the business owner.
        technical_owner: ID of the technical owner.
        organization_unit: Associated organizational unit.
        lifecycle_status: Current lifecycle status (idea | development | testing | deployed | retired).
        eu_ai_act_risk_class: EU AI Act risk class (minimal | limited | high | prohibited).
        human_oversight_description: Description of human oversight measures.
        models: List of AI model IDs used by this system.
    """
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
    """Schema for reading an AI system from the API.
    
    Includes system-generated fields and related objects.
    
    Attributes:
        id: Unique identifier for the system.
        name: Name of the AI system.
        description: Description of the AI system.
        intended_purpose: Intended purpose of the system.
        decision_type: Type of decision (assistive | automated | autonomous).
        business_owner: Business owner user details.
        technical_owner: Technical owner user details.
        organization_unit: Associated organizational unit.
        lifecycle_status: Current lifecycle status.
        eu_ai_act_risk_class: EU AI Act risk class.
        human_oversight_description: Description of human oversight measures.
        models: List of AI models used by this system.
    """
    id: UUID
    name: str
    description: Optional[str]

    intended_purpose: str
    decision_type: Optional[str]

    business_owner: Optional[User]
    technical_owner: Optional[User]

    organization_unit: Optional[str]
    lifecycle_status: Optional[str]
    eu_ai_act_risk_class: Optional[str]

    human_oversight_description: Optional[str]
    
    models: Optional[List[AIModelRead]] 


