from tawala.types.risk_instance import RiskInstance
from tawala.utils.http import HttpClient


class RiskInstanceRepository:
    def __init__(self, http: HttpClient):
        self.http = http

    def list(self) -> list[RiskInstance]:
        response = self.http.get("/risks/instances")
        return [RiskInstance.model_validate(model) for model in response]

    def create(self, data: RiskInstance) -> RiskInstance:
        response = self.http.post("/risks/instances", json=data)
        return RiskInstance.model_validate(response)
    
    def get(self, id: str) -> RiskInstance:
        response = self.http.get(f"/risks/instances/{id}")
        return RiskInstance.model_validate(response)
    
    def update(self, id: str, data) -> RiskInstance:
        response = self.http.put(f"/risks/instances/{id}", json=data)
        return RiskInstance.model_validate(response)