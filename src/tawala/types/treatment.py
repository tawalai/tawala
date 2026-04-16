"""Risk Treatment type definitions for the Tawala SDK.

Defines Pydantic models for creating, updating, and reading risk treatments.
"""
from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

from tawala.types.enums import RiskLevel, TreatmentPriority
from tawala.types.user import User


class RiskTreatmentBase(BaseModel):
    """Base risk treatment model with common attributes.
    
    Attributes:
        treatment: Description of the treatment action.
        effectiveness: Expected or actual effectiveness of the treatment.
        priority: Priority level of the treatment.
        due_date: Due date for completing the treatment.
        resources: Resources required for the treatment.
        monitoring: Monitoring strategy for the treatment.
        residual_risk: Residual risk level after treatment.
        performance_measures: Measures to monitor treatment performance.
        owner_id: ID of the treatment owner.
    """
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
    """Schema for creating a new risk treatment.
    
    Attributes:
        treatment: Description of the treatment action.
        effectiveness: Expected or actual effectiveness of the treatment.
        priority: Priority level of the treatment.
        due_date: Due date for completing the treatment.
        resources: Resources required for the treatment.
        monitoring: Monitoring strategy for the treatment.
        residual_risk: Residual risk level after treatment.
        performance_measures: Measures to monitor treatment performance.
        owner_id: ID of the treatment owner.
        risk_instance_id: ID of the associated risk instance.
    """
    risk_instance_id: UUID


class RiskTreatmentUpdate(RiskTreatmentBase):
    """Schema for updating an existing risk treatment.
    
    All fields are optional to allow partial updates.
    
    Attributes:
        treatment: Description of the treatment action.
        effectiveness: Expected or actual effectiveness of the treatment.
        priority: Priority level of the treatment.
        due_date: Due date for completing the treatment.
        resources: Resources required for the treatment.
        monitoring: Monitoring strategy for the treatment.
        residual_risk: Residual risk level after treatment.
        performance_measures: Measures to monitor treatment performance.
        owner_id: ID of the treatment owner.
    """
    treatment: Optional[str] = None


class RiskTreatmentRead(RiskTreatmentBase):
    """Schema for reading a risk treatment from the API.
    
    Includes system-generated fields and related objects.
    
    Attributes:
        id: Unique identifier for the treatment.
        treatment: Description of the treatment action.
        effectiveness: Expected or actual effectiveness of the treatment.
        priority: Priority level of the treatment.
        due_date: Due date for completing the treatment.
        resources: Resources required for the treatment.
        monitoring: Monitoring strategy for the treatment.
        residual_risk: Residual risk level after treatment.
        performance_measures: Measures to monitor treatment performance.
        owner_id: ID of the treatment owner.
        risk_instance_id: ID of the associated risk instance.
        created_at: Timestamp when the treatment was created.
        updated_at: Timestamp when the treatment was last updated.
        owner: Treatment owner user details.
    """
    id: UUID
    risk_instance_id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None
    owner: Optional[User] = None