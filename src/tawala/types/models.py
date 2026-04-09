# types/models.py
from pydantic import BaseModel

class AIModel(BaseModel):
    id: str
    name: str
    created_at: str