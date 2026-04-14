import json

from tawala.types.ai_model import AIModelCreate, AIModelRead, AIModelUpdate
from tawala.utils.http import HttpClient


class AIModelRepository:
    def __init__(self, http: HttpClient):
        self.http = http
        
    def __objectify(self, data: AIModelCreate | AIModelUpdate):
        return json.loads(data.model_dump_json())

    def list(self) -> list[AIModelRead]:
        response = self.http.get("/ai-portfolio/models")
        return [AIModelRead.model_validate(model) for model in response]

    def create(self, data: AIModelCreate) -> AIModelRead:
        response = self.http.post("/ai-portfolio/models", json=self.__objectify(data))
        return AIModelRead.model_validate(response)
    
    def get(self, id: str) -> AIModelRead:
        response = self.http.get(f"/ai-portfolio/models/{id}")
        return AIModelRead.model_validate(response)
    
    def update(self, id: str, data: AIModelUpdate) -> AIModelRead:
        response = self.http.put(f"/ai-portfolio/models/{id}", json=self.__objectify(data))
        return AIModelRead.model_validate(response)