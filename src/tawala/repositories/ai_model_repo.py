

from tawala.types.ai_model import AIModel
from tawala.utils.http import HttpClient


class AIModelRepository:
    def __init__(self, http: HttpClient):
        self.http = http

    def list(self) -> list[AIModel]:
        return self.http.get("/models")

    def create(self, data) -> AIModel:
        return self.http.post("/models", json=data)
    
    def get(self, id: str) -> AIModel:
        return self.http.get(f"/models/{id}")
    
    def update(self, id: str, data) -> AIModel:
        return self.http.put(f"/models/{id}", json=data)