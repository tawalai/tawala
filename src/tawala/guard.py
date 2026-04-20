

class TawalaGuard:
    def __init__(self, policy_engine):
        self.engine = policy_engine
        
    def evaluate(self, context: dict):
        return self.engine.evaluate(context)