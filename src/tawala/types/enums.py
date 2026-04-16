"""Enumeration types for the Tawala SDK.

Defines enums for risk status, risk levels, and treatment priorities.
"""
from enum import Enum

class RiskStatus(str, Enum):
    """Enumeration of possible risk status values.
    
    Attributes:
        Identified: Risk has been identified.
        UnderTreatment: Risk is currently being treated.
        UnderReview: Risk is being reviewed.
        Closed: Risk has been closed.
    """
    Identified = "Identified"
    UnderTreatment = "Under Treatment"
    UnderReview = "Under Review"
    Closed = "Closed"


class RiskLevel(str, Enum):
    """Enumeration of possible risk levels.
    
    Attributes:
        High: High level risk.
        Medium: Medium level risk.
        Low: Low level risk.
    """
    High = "High"
    Medium = "Medium"
    Low = "Low"


class TreatmentPriority(str, Enum):
    """Enumeration of possible treatment priority levels.
    
    Attributes:
        High: High priority treatment.
        Medium: Medium priority treatment.
        Low: Low priority treatment.
    """
    High = "High"
    Medium = "Medium"
    Low = "Low"
