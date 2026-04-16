"""Risk Review type definitions for the Tawala SDK.

Defines Pydantic models for creating, updating, and reading risk reviews.
"""
from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

from tawala.types.user import User


class RiskReviewBase(BaseModel):
    """Base risk review model with common attributes.
    
    Attributes:
        findings: Findings from the risk review.
        recommendations: Recommendations from the review.
        reviewer_id: ID of the user who performed the review.
    """
    findings: Optional[str] = None
    recommendations: Optional[str] = None
    reviewer_id: UUID

class RiskReviewCreate(RiskReviewBase):
    """Schema for creating a new risk review.
    
    Attributes:
        findings: Findings from the risk review.
        recommendations: Recommendations from the review.
        reviewer_id: ID of the user who performed the review.
        risk_instance_id: ID of the associated risk instance.
    """
    risk_instance_id: UUID

class RiskReviewUpdate(RiskReviewBase):
    """Schema for updating an existing risk review.
    
    Attributes:
        findings: Findings from the risk review.
        recommendations: Recommendations from the review.
        reviewer_id: ID of the user who performed the review.
        reviewed_at: Timestamp when the review was performed.
    """
    reviewed_at: datetime

class RiskReviewRead(RiskReviewBase):
    """Schema for reading a risk review from the API.
    
    Includes system-generated fields and related objects.
    
    Attributes:
        id: Unique identifier for the review.
        findings: Findings from the risk review.
        recommendations: Recommendations from the review.
        reviewer_id: ID of the user who performed the review.
        risk_instance_id: ID of the associated risk instance.
        reviewer: Reviewer user details.
        created_at: Timestamp when the review was created.
        reviewed_at: Timestamp when the review was performed.
        updated_at: Timestamp when the review was last updated.
    """
    id: UUID
    risk_instance_id: UUID
    reviewer: Optional[User] = None
    created_at: datetime
    reviewed_at: datetime
    updated_at: Optional[datetime] = None