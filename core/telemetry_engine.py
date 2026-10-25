import time
import psutil
import json
import os
from core.local_vault import log_telemetry

TAXONOMY_PATH = "config/app_taxonomy.json"

def load_taxonomy():
    if not os.path.exists(TAXONOMY_PATH):
        return {}
    with open(TAXONOMY_PATH, "r") as f:
        return json.load(f).get("categories", {})

def classify_app(app_name):
    taxonomy = load_taxonomy()
    app_lower = app_name.lower()
    
    for cat_name, data in taxonomy.items():
        for known_app in data.get("apps", []):
            if known_app in app_lower:
                return cat_name, data.get("role", "General")
                
    return "decompression", "Unclassified / Neutral"

if __name__ == "__main__":
    print("[✓] Telemetry Engine loaded successfully.")
