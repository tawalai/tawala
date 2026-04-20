from pydantic import BaseModel

from tawala.policy.rule import Rule

class PolicyEngine(BaseModel):
    rules: list[Rule] = []
    
    def evaluate(self, context: dict):
        for rule in self.rules:
            result = rule.apply(context)
            if result['decision'] == 'deny':
                return result
            
        return {'decision': 'allow'}

    def add_rule(self, rule):
        self.rules.append(rule)
        
    def set_rules(self, rules):
        self.rules = rules