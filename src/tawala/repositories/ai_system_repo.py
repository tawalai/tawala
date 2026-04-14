import json

from tawala.types.ai_system import AISystemCreate, AISystemRead, AISystemUpdate
from tawala.utils.http import HttpClient


class AISystemRepository:
    def __init__(self, http: HttpClient):
        self.http = http
        
    def __objectify(self, data: AISystemCreate | AISystemUpdate):
        return json.loads(data.model_dump_json())

    def list(self) -> list[AISystemRead]:
        response = self.http.get("/ai-portfolio/systems")
        return [AISystemRead.model_validate(model) for model in response]

    def create(self, data: AISystemCreate) -> AISystemRead:
        response = self.http.post("/ai-portfolio/systems", json=self.__objectify(data))
        return AISystemRead.model_validate(response)
    
    def get(self, id: str) -> AISystemRead:
        response = self.http.get(f"/ai-portfolio/systems/{id}")
        return AISystemRead.model_validate(response)
    
    def update(self, id: str, data: AISystemUpdate) -> AISystemRead:
        response = self.http.put(f"/ai-portfolio/systems/{id}", json=self.__objectify(data))
        return AISystemRead.model_validate(response)