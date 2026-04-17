"""Example script demonstrating how to create a risk instance.

This example shows how to:
1. Initialize the Tawala client with API credentials
2. Retrieve AI systems and risks from the platform
3. Create a new risk instance associated with a system and risk

Usage:
    Set TAWALA_API_KEY and optionally TAWALA_HOST environment variables,
    then run: python add_risk_instance.py
"""
import os
from tawala import TawalaClient
from tawala.types.ai_system import AISystemRead
from tawala.types.risk import Risk
from tawala.types.risk_instance import RiskInstanceCreate
from tawala.types.enums import RiskLevel, RiskStatus

def main():
    """Create and add a new risk instance to an AI system.
    
    Retrieves the API key and host from environment variables,
    initializes the client, retrieves the first available system and risk,
    and creates a new risk instance with specified parameters.
    """
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