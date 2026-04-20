from tawala.policy.rule import Rule
from transformers import pipeline

class BartLargeTextRule(Rule):
    def apply(self, context: dict, labels=['safe', 'threat']):
        
        classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        result = classifier(context['text'], labels)
        
        threat_index = result['labels'].index('threat')
        threat_score = result['scores'][threat_index]
        
        if threat_score > .5:
            return {"decision": "deny", "reason": 'Threat detected', "risk": "high"}
        
        return {"decision": "allow"}