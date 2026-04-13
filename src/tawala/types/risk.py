from pydantic import BaseModel

class Risk(BaseModel):
    id: str
    title: str
    description: str