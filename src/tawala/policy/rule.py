from pydantic import BaseModel

class Rule(BaseModel):
    def apply(self, context: dict):
        raise NotImplementedError