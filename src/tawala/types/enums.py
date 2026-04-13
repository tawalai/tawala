from enum import Enum

class RiskStatus(str, Enum):
    Identified = "Identified"
    UnderTreatment = "Under Treatment"
    UnderReview = "Under Review"
    Closed = "Closed"


class RiskLevel(str, Enum):
    High = "High"
    Medium = "Medium"
    Low = "Low"


class TreatmentPriority(str, Enum):
    High = "High"
    Medium = "Medium"
    Low = "Low"
