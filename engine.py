from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        """TODO: Return True if all antecedents are true and consequent not yet known."""
        all_antecedents_known = all(ant in self.facts for ant in rule.antecedents)
        consequent_not_known = rule.consequent not in self.facts
        return all_antecedents_known and consequent_not_known

    def run(self) -> None:
        #"""TODO: Implement the forward chaining loop."""
        while True:
            #Find all rules that are eligible to fire
            eligible_rules = [r for r in self.rules if self.can_fire(r)]
            
            if not eligible_rules:
                break  # No more rules can fire, exit the loop
        
            #conflict resolution
            eligible_rules.sort(key=lambda r: r.priority, reverse=True)
            selected_rule = eligible_rules[0]
            
            #Fire rule: assert new fact and record trace
            self.facts.add(selected_rule.consequent)
            self.trace.append({
                "rule_name": selected_rule.name,
                "antecedents": selected_rule.antecedents,
                "consequent": selected_rule.consequent,
                "priority": selected_rule.priority
     })

    def conclusions(self) -> Dict[str, List[str]]:
        #"""TODO: Return separated results (recommendations, specs, other facts)."""
        recommendations = []
        specs = []
        other_facts = []
        
        for fact in sorted(self.facts):
            if fact.startswith("recommend:"):
                recommendations.append(fact.split("recommend:",1)[1])
            elif fact.startswith("spec:"):
                specs.append(fact.split("spec:",1)[1])
            else:
                other_facts.append(fact)
                
        return{
            "recommendations": recommendations,
            "specs": specs,
            "other_facts": other_facts
        }
