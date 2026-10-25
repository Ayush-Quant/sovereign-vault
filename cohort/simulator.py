import random
import json
import os

# Define persona archetypes for the 100-user synthetic cohort
ARCHETYPES = [
    {"role": "Software Engineer", "base_entropy": 0.4, "context_switch_rate": "High"},
    {"role": "Quantitative Analyst", "base_entropy": 0.3, "context_switch_rate": "Medium"},
    {"role": "Product Manager", "base_entropy": 0.7, "context_switch_rate": "Extreme"},
    {"role": "Researcher / Writer", "base_entropy": 0.2, "context_switch_rate": "Low"},
    {"role": "Operations Lead", "base_entropy": 0.6, "context_switch_rate": "High"}
]

def generate_cohort(num_personas=100):
    cohort = []
    for i in range(1, num_personas + 1):
        archetype = random.choice(ARCHETYPES)
        # Add slight variance to base entropy
        entropy_variance = round(random.uniform(-0.15, 0.15), 2)
        simulated_entropy = max(0.0, min(1.0, archetype["base_entropy"] + entropy_variance))
        
        persona = {
            "persona_id": f"USER_{i:03d}",
            "role": archetype["role"],
            "context_switch_rate": archetype["context_switch_rate"],
            "simulated_entropy": simulated_entropy,
            "status": "Burnout Risk" if simulated_entropy > 0.65 else "Balanced"
        }
        cohort.append(persona)
    return cohort

def run_cohort_simulation():
    print("[*] Initializing Synthetic 100-Persona Cohort Simulation...")
    cohort = generate_cohort(100)
    
    burnout_count = sum(1 for p in cohort if p["status"] == "Burnout Risk")
    balanced_count = len(cohort) - burnout_count
    
    print(f"\n[✓] Simulation Complete across {len(cohort)} Synthetic Personas:")
    print(f"    - Balanced Profiles: {balanced_count}")
    print(f"    - High Burnout Risk / Load-Shedding Triggered: {burnout_count}")
    
    # Save output for dashboard display
    os.makedirs("cohort/data", exist_ok=True)
    with open("cohort/data/simulation_results.json", "w") as f:
        json.dump(cohort, f, indent=2)
    print("[✓] Cohort telemetry export saved to cohort/data/simulation_results.json")

if __name__ == "__main__":
    run_cohort_simulation()
