
from tawala.policy.rule import Rule
from tawala.policy.engine import PolicyEngine

class ViolenceRule(Rule):
    def apply(self, context):
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
    
    engine = PolicyEngine()
    engine.add_rule(ViolenceRule())

    sample = {"text": "Do not attack or bomb anyone."}
    result = engine.evaluate(sample)
    
    print(result)