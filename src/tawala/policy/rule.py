"""Base policy rule abstraction for guard rules.

This module defines the base Rule model that all custom policy rules
must extend. A Rule implementation should override the apply method and
return a decision dictionary based on provided context.
"""

from pydantic import BaseModel

class Rule(BaseModel):
    """Base class for a policy rule.

    Subclasses must implement the apply method to evaluate contextual
    input and return a decision object used by the policy engine.
    """

    def apply(self, context: dict):
        """Evaluate the rule against provided context.

        Args:
            context (dict): The evaluation context passed by the policy engine.

        Raises:
            NotImplementedError: When subclasses do not override this method.
        """
        raise NotImplementedError