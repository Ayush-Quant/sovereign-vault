import sqlite3
import json
import os
from datetime import datetime

DB_PATH = "sovereign_vault.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Telemetry session logs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS telemetry_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            app_name TEXT,
            window_title TEXT,
            modality TEXT,
            dwell_seconds INTEGER,
            entropy_score REAL
        )
    ''')
    
    # User resilience vault & reflections
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resilience_vault (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            stressor_input TEXT,
            socratic_output TEXT,
            action_taken TEXT
        )
    ''')
    
    # Zero-cost semantic cache for Nebius & Tavily calls
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS api_cache (
            cache_key TEXT PRIMARY KEY,
            response_json TEXT,
            timestamp TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def log_telemetry(app_name, window_title, modality, dwell_seconds, entropy_score):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO telemetry_logs (timestamp, app_name, window_title, modality, dwell_seconds, entropy_score)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (datetime.now().isoformat(), app_name, window_title, modality, dwell_seconds, entropy_score))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("[✓] Local SQLite Vault initialized successfully at sovereign_vault.db")
