import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.search_engine import fetch_cognitive_research

load_dotenv()

client = OpenAI(
    base_url="https://api.tokenfactory.us-north1.nebius.com/v1/",
    api_key=os.getenv("NEBIUS_API_KEY")
)

def generate_socratic_reframing(entropy_score, recent_activity):
    live_research = fetch_cognitive_research(query="attention residue cognitive ergonomics deep work interruption recovery")

    system_prompt = (
        "You are Sovereign Vault, an uncompromising, high-precision Cognitive Guardian agent. "
        "Your job is to protect working memory against information overload and context-switching friction. "
        "Never offer generic, vague wellness advice or soft platitudes. "
        "Instead, provide direct, highly actionable load-shedding interventions grounded in cognitive ergonomics. "
        "Give concrete commands or sharp choices: specify exactly what to close, how to bundle notifications, "
        "or how to write an explicit 'ready-to-resume' bridge before a transition."
    )
    
    user_prompt = (
        f"Telemetry Alert: Current cognitive entropy score is {entropy_score} (scale 0 to 1). "
        f"Active Telemetry Context: {recent_activity}.\n\n"
        f"Live Cognitive Ergonomics Research Context:\n{live_research}\n\n"
        "Deliver a sharp, authoritative load-shedding directive or a precise structural intervention "
        "that forces an immediate reduction in cognitive load."
    )

    try:
        response = client.chat.completions.create(
            model="nvidia/Nemotron-3.5-Super-VL",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=3000,  # Increased to 3000 to prevent text cutoff
            temperature=0.3
        )
        message = response.choices[0].message
        content = getattr(message, "content", None)
        
        if not content:
            return "Load-Shedding Protocol Active: Close all secondary communication windows immediately. Write down your exact next line of code or text on a physical scratchpad, then enforce a 15-minute single-app window."
            
        return content.strip()
    except Exception as e:
        return f"[!] Agent Error: {e}"

if __name__ == "__main__":
    print("[*] Testing Socratic Guardian Agent with High-Impact Directive...")
    sample_response = generate_socratic_reframing(0.85, "Antigravity, MS Word, MS PowerPoint, Slack, Browser Tabs (x12)")
    print(f"\n[Guardian Output]:\n{sample_response}")
