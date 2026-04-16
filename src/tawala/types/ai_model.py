
"""AI Model type definitions for the Tawala SDK.

Defines Pydantic models for creating, updating, and reading AI models.
"""
from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class AIModelCreate(BaseModel):
    """Schema for creating a new AI model.
    
    Attributes:
        name: Name of the AI model.
        model_type: Type or category of the model.
        provider: Organization or provider of the model.
        version: Version of the model.
        training_date: Date when the model was trained.
        training_data_description: Description of training data used.
        evaluation_metrics: Metrics from model evaluation.
        known_limitations: Known limitations of the model.
        update_policy: Policy for model updates.
    """
    name: str
    model_type: str

    provider: Optional[str] = None
    version: Optional[str] = None
    training_date: Optional[date] = None

    training_data_description: Optional[str] = None
    evaluation_metrics: Optional[dict] = None
    known_limitations: Optional[str] = None
    update_policy: Optional[str] = None


class AIModelUpdate(BaseModel):
    """Schema for updating an existing AI model.
    
    All fields are optional to allow partial updates.
    
    Attributes:
        name: Name of the AI model.
        model_type: Type or category of the model.
        provider: Organization or provider of the model.
        version: Version of the model.
        training_date: Date when the model was trained.
        training_data_description: Description of training data used.
        evaluation_metrics: Metrics from model evaluation.
        known_limitations: Known limitations of the model.
        update_policy: Policy for model updates.
    """
    name: Optional[str] = None
    model_type: Optional[str] = None
    provider: Optional[str] = None
    version: Optional[str] = None

    training_date: Optional[date] = None
    training_data_description: Optional[str] = None
    evaluation_metrics: Optional[dict] = None
    known_limitations: Optional[str] = None
    update_policy: Optional[str] = None


class AIModelRead(BaseModel):
    """Schema for reading an AI model from the API.
    
    Includes system-generated fields like ID and timestamps.
    
    Attributes:
        id: Unique identifier for the model.
        name: Name of the AI model.
        model_type: Type or category of the model.
        created_at: Timestamp when the model was created.
        updated_at: Timestamp when the model was last updated.
        provider: Organization or provider of the model.
        version: Version of the model.
        training_date: Date when the model was trained.
        training_data_description: Description of training data used.
        evaluation_metrics: Metrics from model evaluation.
        known_limitations: Known limitations of the model.
        update_policy: Policy for model updates.
    """
    id: UUID
    name: str
    model_type: str
    created_at: datetime
    updated_at: datetime

    provider: Optional[str]
    version: Optional[str]

    training_date: Optional[date] = None
    training_data_description: Optional[str]
    evaluation_metrics: Optional[dict]
    known_limitations: Optional[str]
    update_policy: Optional[str]