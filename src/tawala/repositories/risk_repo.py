from tawala.types.risk import Risk
from tawala.utils.http import HttpClient


class RiskRepository:
    def __init__(self, http: HttpClient):
        self.http = http

    def list(self) -> list[Risk]:
        response = self.http.get("/risks")
        return [Risk.model_validate(model) for model in response]

    def create(self, data: Risk) -> Risk:
        response = self.http.post("/risks", json=data)
        return Risk.model_validate(response)
    
    def get(self, id: str) -> Risk:
        response = self.http.get(f"/risks/{id}")
        return Risk.model_validate(response)
    
    def update(self, id: str, data) -> Risk:
        response = self.http.put(f"/risks/{id}", json=data)
        return Risk.model_validate(response)