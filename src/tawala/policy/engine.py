"""Policy engine for evaluating rules against request context.

This module provides a simple policy engine that applies registered rules
sequentially. The engine returns the first deny decision encountered, or allows
content when no rule denies it.
"""

from pydantic import BaseModel

from tawala.policy.rule import Rule

class PolicyEngine(BaseModel):
    """Engine that evaluates policy rules in order.

    The engine stores a list of Rule instances and uses them to make a
    decision for an incoming context payload.
    """

    rules: list[Rule] = []
    
    def evaluate(self, context: dict):
        """Evaluate the context against all registered rules.

        Args:
            context (dict): Contextual data passed to each rule.

        Returns:
            dict: The first rule result with decision 'deny', or a default
                allow decision if no rule denies the request.
        """
        for rule in self.rules:
            result = rule.apply(context)
            if result['decision'] == 'deny':
                return result
            
        return {'decision': 'allow'}

    def add_rule(self, rule):
        """Register a new rule with the engine."""
        self.rules.append(rule)
        
    def set_rules(self, rules):
        """Replace the engine's rule set."""
        self.rules = rules