"""Guard wrapper around a policy engine.

This module exposes TawalaGuard as a lightweight wrapper that delegates
context evaluation to a PolicyEngine instance.
"""

import logging
from tawala.policy.engine import PolicyEngine
from tawala.utils.tawala_logger import TawalaLogger

class TawalaGuard:
    """High-level guard that evaluates input using a policy engine."""

    def __init__(self, policy_engine: PolicyEngine, debug: bool = False):
        """Initialize the guard with a PolicyEngine instance."""
        
        self.logger = TawalaLogger(name="tawala.guard").get_logger()
        
        if debug:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
        
        self.engine = policy_engine
        
    def evaluate(self, context: dict):
        """Evaluate context through the configured policy engine.

        Args:
            context (dict): The context data to evaluate.

        Returns:
            dict: The policy engine result.
        """
        
        if self.logger:
            self.logger.debug(f"Evaluating context: {context}")
        
        return self.engine.evaluate(context)