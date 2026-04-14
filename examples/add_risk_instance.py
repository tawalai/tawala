import json
import os
from tawala.client import TawalaClient
from tawala.types.ai_system import AISystemRead
from tawala.types.risk import Risk
from tawala.types.risk_instance import RiskInstanceCreate
from tawala.types.enums import RiskLevel, RiskStatus

def main():
    api_key = os.getenv("TAWALA_API_KEY", "YOUR_API_KEY")
    tawala_host = os.getenv("TAWALA_HOST", "https://platformapi.tawala.ai")
    client: TawalaClient = TawalaClient(api_key=api_key, base_url=tawala_host)
    system_list: list[AISystemRead] = client.systems.list()
    
    system = system_list[0]
    
    risks: list[Risk] = client.risks.list()
    risk: Risk = risks[0]
    
    risk_instance: RiskInstanceCreate = RiskInstanceCreate(
        ai_system_id=system.id,
        risk_id=risk.id,
        likelihood=RiskLevel.High,
        impact=RiskLevel.High,
        residual=RiskLevel.High,
        status=RiskStatus.Identified
    )
    
    client.risk_instances.create(risk_instance)
    
    
    
if __name__ == "__main__":
    main()