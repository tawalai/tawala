from tawala.types.ai_model import AIModel
from tawala.utils.http import HttpClient


class AIModelRepository:
    def __init__(self, http: HttpClient):
        self.http = http

    def list(self) -> list[AIModel]:
        response = self.http.get("/models")
        return [AIModel.model_validate(model) for model in response]

    def create(self, data: AIModel) -> AIModel:
        response = self.http.post("/models", json=data)
        return AIModel.model_validate(response)
    
    def get(self, id: str) -> AIModel:
        response = self.http.get(f"/models/{id}")
        return AIModel.model_validate(response)
    
    def update(self, id: str, data) -> AIModel:
        response = self.http.put(f"/models/{id}", json=data)
        return AIModel.model_validate(response)