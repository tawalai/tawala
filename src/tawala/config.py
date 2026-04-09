from pydantic import BaseModel

class Config(BaseModel):
    api_key: str
    base_url: str