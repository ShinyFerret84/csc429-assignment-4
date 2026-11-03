from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    # TODO: Ask more questions to collect facts for reasoning
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
        
    if input("Is your budget high? (y/n): ").lower().startswith("y"):
        facts.append("budget_high")
    elif input("Is your budget low? (y/n): ").lower().startswith("y"):
        facts.append("budget_low")
    elif input("Is your budget medium? (y/n): ").lower().startswith("y"):
        facts.append("budget_medium")
        
    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
        
    if input("Will you use the laptop for gaming? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Will you perform creative work (e.g., video editing)? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Is your usage for basic office/study work only? (y/n): ").lower().startswith("y"):
        facts.append("office_only")
        
    if input("Do you prefer a large screen (15\"+)? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    if input("Do you require AI acceleration / tensor cores? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")

    if input("Do you prefer macOS? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_macos")
    elif input("Do you prefer Linux? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_linux")
    
    return facts

def main():
    # TODO: Load rules, create engine, assert facts, and run inference
    
    #load rules from knowledge base
    rules = load_rules(KB_PATH)
    print(f"Loaded {len(rules)} rules from knowledge base.")
    
    #gather initial facts from user input
    initial_facts = collect_initial_facts()
    print(f"\nInitial facts: {initial_facts}\n")
    
    #create engine, assert initial facts, run engine
    engine = ForwardChainingEngine(rules)
    engine.assert_facts(initial_facts)
    engine.run()
    
    #extract and display conclusions
    results = engine.conclusions()
    
    if results["recommendations"]:
        for rec in results["recommendations"]:
            print(f"Recommendation: {rec}")
            
    else: 
        print("No recommendations could be made based on the provided facts.")
        
    if results["specs"]:
        for spec in results["specs"]:
            print(f"Specification: {spec}")

    print("\n--- Fired Rules Explanation Trace ---")
    if engine.trace:
        for idx, step in enumerate(engine.trace, start=1):
            print(f"Step {idx}: Fired '{step['rule_name']}' (Priority {step['priority']})")
            print(f"        IF {step['antecedents']} THEN {step['consequent']}")
    else:
        print("No rules fired.")
                

if __name__ == "__main__":
    main()
