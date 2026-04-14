import json
from tawala.types.risk_instance import RiskInstanceCreate, RiskInstanceRead, RiskInstanceUpdate
from tawala.utils.http import HttpClient


class RiskInstanceRepository:
    def __init__(self, http: HttpClient):
        self.http = http
        
    def __objectify(self, data: RiskInstanceCreate | RiskInstanceUpdate):
        return json.loads(data.model_dump_json())

    def list(self) -> list[RiskInstanceRead]:
        response = self.http.get("/risks/instances")
        return [RiskInstanceRead.model_validate(model) for model in response]

    def create(self, data: RiskInstanceCreate) -> RiskInstanceRead:
        response = self.http.post("/risks/instances", json=self.__objectify(data))
        return RiskInstanceRead.model_validate(response)
    
    def get(self, id: str) -> RiskInstanceRead:
        response = self.http.get(f"/risks/instances/{id}")
        return RiskInstanceRead.model_validate(response)
    
    def update(self, id: str, data: RiskInstanceUpdate) -> RiskInstanceRead:
        response = self.http.put(f"/risks/instances/{id}", json=data)
        return RiskInstanceRead.model_validate(response)