
"""Example demonstrating how to create and apply a custom guard rule.

This example shows how to implement a custom Rule that detects violent language,
apply it through a PolicyEngine, and create risk instances in the Tawala system
when policy violations are detected.
"""
import os
from tawala import TawalaClient

from tawala.policy.rule import Rule
from tawala.policy.engine import PolicyEngine
from tawala.types.ai_system import AISystemRead
from tawala.types.enums import RiskLevel, RiskStatus
from tawala.types.risk import Risk
from tawala.types.risk_instance import RiskInstanceCreate

class ViolenceRule(Rule):
    """Custom rule that detects violent keywords in text content.
    
    This rule checks for the presence of violent keywords (kill, attack, bomb)
    in the provided context and denies requests that contain them.
    """
    
    def apply(self, context):
        """Apply the violence detection rule.
        
        Args:
            context (dict): A dictionary containing contextual information,
                expected to have a 'text' key with string content to evaluate.
        
        Returns:
            dict: A decision dictionary with keys:
                - 'decision' (str): Either 'allow' or 'deny'
                - 'reason' (str): Optional explanation of the decision
                - 'risk' (str): Optional risk level assessment
        """
        keywords = ["kill", "attack", "bomb"]
        
        text = context.get("text", "").lower()

        for word in keywords:
            if word in text:
                return {
                    "decision": "deny",
                    "reason": f"Violent keyword detected: {word}",
                    "risk": "high"
                }

        return {"decision": "allow"}


if __name__ == "__main__":
  
    api_key = os.getenv("TAWALA_API_KEY", "YOUR_API_KEY")
    tawala_host = os.getenv("TAWALA_HOST", "https://platformapi.tawala.ai")
    
    client = TawalaClient(api_key=api_key, base_url=tawala_host)
    system: AISystemRead = client.systems.list()[0]
    
    engine = PolicyEngine()
    engine.add_rule(ViolenceRule())

    sample = {"text": "Do not attack or bomb anyone."}
    result = engine.evaluate(sample)
    
    if result['decision'] == 'deny':
    
        risk: Risk = client.risks.list()[0]
    
        risk_instance: RiskInstanceCreate = RiskInstanceCreate(
            ai_system_id=system.id,
            risk_id=risk.id,
            likelihood=RiskLevel.High,
            impact=RiskLevel.High,
            residual=RiskLevel.High,
            status=RiskStatus.Identified
        )
    
        client.risk_instances.create(risk_instance)
        
        print("Risk instance created:", risk_instance)