"""Guard wrapper around a policy engine.

This module exposes TawalaGuard as a lightweight wrapper that delegates
context evaluation to a PolicyEngine instance.
"""

from tawala.policy.engine import PolicyEngine

class TawalaGuard:
    """High-level guard that evaluates input using a policy engine."""

    def __init__(self, policy_engine: PolicyEngine):
        """Initialize the guard with a PolicyEngine instance."""
        self.engine = policy_engine
        
    def evaluate(self, context: dict):
        """Evaluate context through the configured policy engine.

        Args:
            context (dict): The context data to evaluate.

        Returns:
            dict: The policy engine result.
        """
        return self.engine.evaluate(context)