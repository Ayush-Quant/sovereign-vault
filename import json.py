import os
from openai import OpenAI

def generate_socratic_reframing(entropy_index, active_apps):
    # Initialize the OpenAI-compatible Nebius Token Factory client
    client = OpenAI(
        base_url="https://api.studio.nebius.ai/v1",
        api_key=os.environ.get("NEBIUS_API_KEY"),
    )
    
    try:
        response = client.chat.completions.create(
            # Using your fine-tuned model endpoint/checkpoint identifier
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=[
                {
                    "role": "system",
                    "content": "You are the Sovereign Vault Socratic Guardian. Deliver aggressive, high-precision cognitive load-shedding directives based on population stress telemetry."
                },
                {
                    "role": "user",
                    "content": f"Entropy Index: {entropy_index}. Active Processes: {active_apps}."
                }
            ],
            temperature=0.7,
            max_tokens=400
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Socratic Guardian Offline: Unable to compute cognitive vector ({e})."