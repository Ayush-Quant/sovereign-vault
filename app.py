import streamlit as st
import time
import pandas as pd
import json
import os
import requests
from core.agent_engine import generate_socratic_reframing
from core.local_vault import init_db
from cohort.simulator import run_cohort_simulation

st.set_page_config(
    page_title="Sovereign Vault | Biometric Cognitive Monitor",
    page_icon="🛡️",
    layout="wide"
)

# --- BIOMETRIC & SAAS DESIGN SYSTEM (Inspired by High-End Health/ECG UIs) ---
st.markdown("""
<style>
    /* Global Background & Typography */
    .stApp {
        background-color: #050508;
        color: #f1f5f9;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Top Header Bar */
    .biometric-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.25rem 1.5rem;
        background: rgba(17, 24, 39, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 16px;
        backdrop-filter: blur(12px);
        margin-bottom: 2rem;
    }
    
    .brand-title {
        font-size: 1.25rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        color: #ffffff;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .live-badge {
        background-color: rgba(16, 185, 129, 0.1);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.2);
        padding: 0.3rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .alert-badge {
        background-color: rgba(239, 68, 68, 0.1);
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.2);
        padding: 0.3rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Biometric Card Containers */
    .bio-card {
        background: rgba(13, 17, 23, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 16px;
        padding: 1.75rem;
        margin-bottom: 1.25rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }
    
    .bio-card-critical {
        background: linear-gradient(145deg, rgba(20, 10, 10, 0.9) 0%, rgba(13, 17, 23, 0.9) 100%);
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 16px;
        padding: 1.75rem;
        margin-bottom: 1.25rem;
        box-shadow: 0 10px 30px rgba(239, 68, 68, 0.1);
    }

    /* Process Tags (Pills) */
    .process-pill-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 0.75rem;
        margin-bottom: 0.75rem;
    }
    
    .process-pill {
        background: rgba(99, 102, 241, 0.1);
        color: #a5b4fc;
        border: 1px solid rgba(99, 102, 241, 0.2);
        padding: 0.35rem 0.85rem;
        border-radius: 8px;
        font-size: 0.8rem;
        font-family: monospace;
        font-weight: 600;
    }

    /* Custom Streamlit Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%) !important;
        color: #ffffff !important;
        font-weight: 600;
        border: none;
        border-radius: 10px;
        padding: 0.7rem 1.5rem;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4);
        transition: all 0.2s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #4338ca 0%, #4f46e5 100%) !important;
        box-shadow: 0 6px 20px rgba(79, 70, 229, 0.6);
        transform: translateY(-1px);
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #0b0f19;
        padding: 6px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.06);
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        color: #94a3b8;
        font-weight: 600;
        padding: 10px 20px;
    }

    .stTabs [aria-selected="true"] {
        background-color: #1e293b !important;
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize database
init_db()

# Top Biometric Header
st.markdown("""
<div class="biometric-header">
    <div class="brand-title">
        <span>🛡️</span> SOVEREIGN VAULT <span style="font-size: 0.75rem; font-weight: 400; color: #64748b;">// BIOMETRIC COGNITIVE MONITOR</span>
    </div>
    <div>
        <span class="live-badge">● PERIMETER SECURE</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Main Navigation Tabs
tab1, tab2, tab3 = st.tabs(["⚡ Live Telemetry & ECG", "🌐 Population Matrix", "📋 Feedback Vault"])

with tab1:
    # Sidebar Controls styled as Biometric Deck
    st.sidebar.markdown("### 🎛️ Telemetry Calibration")
    st.sidebar.markdown("Adjust working memory strain parameters.")
    simulated_entropy = st.sidebar.slider("Cognitive Entropy Index", 0.0, 1.0, 0.85, 0.05)
    
    st.sidebar.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    st.sidebar.markdown("### 🔍 Active Process Context")
    app_input = st.sidebar.text_area("Currently Active Windows/Tabs", "Antigravity, MS Word, Slack, Browser Tabs (x14)")
    
    # Parse apps into neat clean biometric pills
    apps_list = [app.strip() for app in app_input.split(",") if app.strip()]

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("### 📈 Brain Entropy Vital Stream")
        
        if simulated_entropy > 0.7:
            st.markdown(f"""
            <div class="bio-card-critical">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 700; color: #f87171; font-size: 0.85rem; letter-spacing: 0.05em;">STATE: ATTENTION RESIDUE OVERLOAD</span>
                    <span class="alert-badge">Critical Risk</span>
                </div>
                <div style="font-size: 3.5rem; font-weight: 800; color: #ffffff; margin: 0.5rem 0; letter-spacing: -0.03em;">
                    {simulated_entropy * 100:.0f}<span style="font-size: 1.5rem; color: #f87171; font-weight: 600;">%</span>
                </div>
                <p style="color: #94a3b8; font-size: 0.9rem; margin: 0;">High context-switching frequency detected. Estimated cognitive penalty: ~23 minutes per switch.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="bio-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 700; color: #34d399; font-size: 0.85rem; letter-spacing: 0.05em;">STATE: DEEP FOCUS BASELINE</span>
                    <span class="live-badge">Optimal</span>
                </div>
                <div style="font-size: 3.5rem; font-weight: 800; color: #ffffff; margin: 0.5rem 0; letter-spacing: -0.03em;">
                    {simulated_entropy * 100:.0f}<span style="font-size: 1.5rem; color: #34d399; font-weight: 600;">%</span>
                </div>
                <p style="color: #94a3b8; font-size: 0.9rem; margin: 0;">Working memory perimeter secure. Friction levels within safe tolerance.</p>
            </div>
            """, unsafe_allow_html=True)

        # Render Active Process Context as Neatly Styled Chips/Pills
        st.markdown("#### 🔗 Active Friction Sources")
        pills_html = "".join([f'<span class="process-pill">{app}</span>' for app in apps_list])
        st.markdown(f'<div class="process-pill-container">{pills_html}</div>', unsafe_allow_html=True)

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        
        chart_data = pd.DataFrame({
            "Time Window": [f"T-{i}" for i in range(10, 0, -1)],
            "Entropy Index": [0.2, 0.3, 0.35, 0.45, 0.55, 0.65, 0.7, 0.8, 0.82, simulated_entropy]
        })
        st.line_chart(chart_data, x="Time Window", y="Entropy Index", color="#6366f1")

    with col2:
        st.markdown("### 🧠 Nemotron Socratic Interceptor")
        st.markdown("Execute real-time load-shedding to clear working memory.")
        
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        
        if st.button("🚨 EXECUTE LOAD-SHEDDING PROTOCOL"):
            with st.spinner("Nebius Token Factory computing cognitive vector..."):
                guardian_response = generate_socratic_reframing(simulated_entropy, app_input)
                st.markdown(f"""
                <div class="bio-card-critical" style="margin-top: 0.5rem;">
                    <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
                        <span style="color: #f87171; font-size: 1.2rem;">🛡️</span>
                        <strong style="color: #ffffff; letter-spacing: 0.05em; font-size: 0.95rem;">GUARDIAN INTERVENTION DIRECTIVE</strong>
                    </div>
                    <div style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.7; white-space: pre-wrap; font-family: monospace;">{guardian_response}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="bio-card" style="text-align: center; padding: 3rem 1.5rem;">
                <div style="font-size: 2.5rem; margin-bottom: 1rem;">🛡️</div>
                <p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 1.5rem;">System on standby. Trigger the interceptor to evaluate telemetry and receive your tailored load-shedding directive.</p>
                <span style="display: inline-block; padding: 0.4rem 0.85rem; background: rgba(99, 102, 241, 0.1); color: #818cf8; border-radius: 8px; font-size: 0.8rem; font-weight: 600; border: 1px solid rgba(99, 102, 241, 0.2);">Engine: nvidia/Nemotron-3.5-Super-VL</span>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("### 🌐 Population Stress Matrix (100-Persona Cohort)")
    st.markdown("Evaluating autonomous load-shedding efficacy and burnout thresholds across diverse professional archetypes.")
    
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    
    col_btn, _ = st.columns([1, 3])
    with col_btn:
        if st.button("🔄 RE-RUN SIMULATION MATRIX"):
            run_cohort_simulation()
            st.success("Simulation matrix refreshed.")

    cohort_file = "cohort/data/simulation_results.json"
    if os.path.exists(cohort_file):
        with open(cohort_file, "r") as f:
            cohort_data = json.load(f)
            
        df_cohort = pd.DataFrame(cohort_data)
        
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Cohort Nodes", len(df_cohort))
        c2.metric("Balanced Operatives", len(df_cohort[df_cohort["status"] == "Balanced"]))
        c3.metric("Burnout Intercepts Triggered", len(df_cohort[df_cohort["status"] == "Burnout Risk"]))
        
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        st.markdown("#### Detailed Persona Telemetry")
        st.dataframe(df_cohort, use_container_width=True, height=400)
    else:
        st.warning("No simulation telemetry detected. Click 'Re-run Simulation Matrix' above.")

with tab3:
    st.markdown("### 📋 User Feedback & Telemetry Log")
    st.markdown("Submit your testing feedback directly into our secure Google Sheets vault.")
    
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    
    with st.form("feedback_form"):
        fb_name = st.text_input("Your Name")
        fb_email = st.text_input("Your Email Address")
        fb_feedback = st.text_area("Your Feedback / Comments")
        
        submitted = st.form_submit_button("Submit Feedback to Google Sheets")
        if submitted:
            if fb_name and fb_email and fb_feedback:
                # Replace with your actual Google Apps Script Web App URL
                WEB_APP_URL = "https://script.google.com/macros/s/AKfycbz.../exec"
                
                payload = {
                    "name": fb_name,
                    "email": fb_email,
                    "feedback": fb_feedback
                }
                
                try:
                    response = requests.post(WEB_APP_URL, json=payload)
                    if response.status_code == 200:
                        st.success("Thank you! Your feedback has been securely logged to the Google Sheet.")
                    else:
                        st.error("Failed to log feedback. Please check your Web App URL.")
                except Exception as e:
                    st.error(f"Connection error: {e}")
            else:
                st.warning("Please fill out all fields before submitting.")

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<p style='text-align: center; color: #475569; font-size: 0.8rem;'>SOVEREIGN VAULT // BIOMETRIC COGNITIVE GUARD & LOAD-SHEDDING ENGINE</p>", unsafe_allow_html=True)
