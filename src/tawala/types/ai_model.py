# types/models.py
from pydantic import BaseModel

class AIModel(BaseModel):
    id: str
    name: str
    model_type: str