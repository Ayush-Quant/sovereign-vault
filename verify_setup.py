import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

NEBIUS_API_KEY = os.getenv("NEBIUS_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def verify_nebius_and_nemotron():
    print("=== Testing Nebius Token Factory (us-north1) ===")
    if not NEBIUS_API_KEY:
        print("[!] ERROR: NEBIUS_API_KEY is missing.")
        return

    # Updated with the exact regional base URL from your dashboard
    client = OpenAI(
        base_url="https://api.tokenfactory.us-north1.nebius.com/v1/",
        api_key=NEBIUS_API_KEY
    )

    try:
        print("[*] Sending inference request to nvidia/Nemotron-3.5-Super-VL...")
        t0 = time.time()
        resp = client.chat.completions.create(
            model="nvidia/Nemotron-3.5-Super-VL",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": [{"type": "text", "text": "Confirm Sovereign Vault telemetry link is online in 10 words or less."}]}
            ],
            max_tokens=30
        )
        latency = round((time.time() - t0) * 1000, 1)
        print(f"[✓] Success! ({latency} ms)")
        print(f"[✓] Response: {resp.choices[0].message.content.strip()}")

    except Exception as e:
        print(f"[!] Nebius API Error Details: {e}")

if __name__ == "__main__":
    verify_nebius_and_nemotron()
