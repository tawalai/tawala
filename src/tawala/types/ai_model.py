

from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class AIModelCreate(BaseModel):
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