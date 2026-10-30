import json

# Load your population stress matrix data
with open("cohort/data/simulation_results.json", "r") as f:
    cohort_data = json.load(f)

dataset = []

for person in cohort_data:
    name = person.get("name", "Operative")
    archetype = person.get("archetype", "Professional")
    entropy = person.get("entropy_index", 0.75)
    status = person.get("status", "Balanced")
    apps = person.get("active_apps", "Slack, Chrome, IDE")
    
    # Define system prompt defining the Socratic Guardian persona
    system_prompt = "You are the Sovereign Vault Socratic Guardian. Deliver aggressive, high-precision cognitive load-shedding directives based on population stress telemetry."
    
    # Construct the user input matching your app interface
    user_content = f"Archetype: {archetype} ({name}). Entropy Index: {entropy}. Status: {status}. Active Processes: {apps}."
    
    # Construct the expert assistant response based on status
    if status == "Burnout Risk":
        assistant_content = f"🚨 CRITICAL COGNITIVE INTERCEPT ({entropy * 100:.0f}% Entropy - {status.upper()}).\n\nDIRECTIVE FOR {archetype.upper()}:\n1. Immediate termination of ambient background loops ({apps}).\n2. Enforce a 30-minute deep-work isolation protocol to clear working memory residue."
    else:
        assistant_content = f"🟢 OPTIMAL BASELINE ({entropy * 100:.0f}% Entropy - {status.upper()}).\n\nDIRECTIVE:\nPerimeter secure. Maintain current operational cadence across {apps}."

    dataset.append({
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": assistant_content}
        ]
    })

# Save out to JSONL for Nebius Socratic Fine-Tuning
with open("socratic_training_data.jsonl", "w") as out:
    for item in dataset:
        out.write(json.dumps(item) + "\n")

print(f"Successfully generated {len(dataset)} training rows in socratic_training_data.jsonl!")