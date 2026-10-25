import streamlit as st
import time
import pandas as pd
import json
import os
from core.agent_engine import generate_socratic_reframing
from core.local_vault import init_db
from cohort.simulator import run_cohort_simulation

st.set_page_config(
    page_title="Sovereign Vault | Cognitive Intelligence",
    page_icon="🛡️",
    layout="wide"
)

# --- ELITE SAAS DESIGN SYSTEM (Linear / Vercel Inspired) ---
st.markdown("""
<style>
    /* Global Page Styling */
    .stApp {
        background-color: #090d16;
        color: #f3f4f6;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Clean Top Header / Nav Bar */
    .app-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.5rem 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 2rem;
    }
    
    .brand-title {
        font-size: 1.5rem;
        font-weight: 700;
        letter-spacing: -0.025em;
        color: #ffffff;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .status-badge {
        background-color: rgba(16, 185, 129, 0.1);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.2);
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .status-badge-alert {
        background-color: rgba(239, 68, 68, 0.1);
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.2);
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Modern Card Containers */
    .saas-card {
        background-color: #111827;
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    .saas-card-highlight {
        background: linear-gradient(145deg, #111827 0%, #1f2937 100%);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
    }

    /* Typography Overrides */
    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 600;
        letter-spacing: -0.025em;
    }
    
    p, span, label {
        color: #9ca3af;
    }

    /* Streamlit Button Overrides (SaaS Gradient Style) */
    .stButton>button {
        background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%) !important;
        color: #ffffff !important;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.25rem;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
        transition: all 0.2s ease;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #4338ca 0%, #4f46e5 100%) !important;
        box-shadow: 0 6px 16px rgba(79, 70, 229, 0.5);
        transform: translateY(-1px);
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #0b0f19;
        padding: 4px;
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.06);
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 6px;
        color: #9ca3af;
        font-weight: 500;
        padding: 8px 16px;
    }

    .stTabs [aria-selected="true"] {
        background-color: #1f2937 !important;
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize database
init_db()

# Custom Header
st.markdown("""
<div class="app-header">
    <div class="brand-title">
        <span>🛡️</span> Sovereign Vault <span style="font-size: 0.85rem; font-weight: 400; color: #6b7280; margin-left: 0.5rem;">Cognitive Intelligence Engine</span>
    </div>
    <div>
        <span class="status-badge">● Secure Bastion Active</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Main Navigation Tabs
tab1, tab2 = st.tabs(["⚡ Live Telemetry & Guardian", "�� Population Stress Matrix"])

with tab1:
    # Sidebar Controls
    st.sidebar.markdown("### 🎛️ Telemetry Parameters")
    st.sidebar.markdown("Simulate active working memory pressure.")
    simulated_entropy = st.sidebar.slider("Cognitive Entropy Index", 0.0, 1.0, 0.85, 0.05)
    recent_apps = st.sidebar.text_input("Active Process Context", "Antigravity, MS Word, Slack, Browser Tabs (x14)")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("### 📊 Entropy & Friction Stream")
        
        if simulated_entropy > 0.7:
            st.markdown(f"""
            <div class="saas-card" style="border-left: 4px solid #ef4444;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 600; color: #f87171;">CRITICAL FRICTION SPIKE</span>
                    <span class="status-badge-alert">Risk: High</span>
                </div>
                <h2 style="margin: 0.5rem 0 0.25rem 0; font-size: 2rem;">{simulated_entropy * 100:.0f}%</h2>
                <p style="margin: 0; font-size: 0.875rem;">Attention residue overload. Estimated cognitive penalty: ~23 minutes per context switch.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="saas-card" style="border-left: 4px solid #10b981;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 600; color: #34d399;">STABLE BASELINE</span>
                    <span class="status-badge">Optimal</span>
                </div>
                <h2 style="margin: 0.5rem 0 0.25rem 0; font-size: 2rem;">{simulated_entropy * 100:.0f}%</h2>
                <p style="margin: 0; font-size: 0.875rem;">Working memory perimeter secure. Minimal friction detected.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        
        chart_data = pd.DataFrame({
            "Time Window": [f"T-{i}" for i in range(10, 0, -1)],
            "Entropy Index": [0.2, 0.3, 0.35, 0.45, 0.55, 0.65, 0.7, 0.8, 0.82, simulated_entropy]
        })
        st.line_chart(chart_data, x="Time Window", y="Entropy Index", color="#6366f1")

    with col2:
        st.markdown("### 🧠 Nemotron Socratic Interceptor")
        st.markdown("Execute autonomous load-shedding to clear working memory.")
        
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        
        if st.button("🚨 EXECUTE LOAD-SHEDDING PROTOCOL"):
            with st.spinner("Nebius Token Factory computing cognitive vector..."):
                guardian_response = generate_socratic_reframing(simulated_entropy, recent_apps)
                st.markdown(f"""
                <div class="saas-card-highlight" style="margin-top: 1rem;">
                    <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.75rem;">
                        <span style="color: #6366f1; font-size: 1.2rem;">🛡️</span>
                        <strong style="color: #ffffff; letter-spacing: 0.025em;">GUARDIAN DIRECTIVE</strong>
                    </div>
                    <div style="color: #e5e7eb; font-size: 0.95rem; line-height: 1.6; white-space: pre-wrap;">{guardian_response}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="saas-card" style="text-align: center; padding: 2.5rem 1.5rem;">
                <p style="color: #6b7280; margin-bottom: 1rem;">System on standby. Trigger the interceptor to evaluate telemetry and receive your tailored load-shedding directive.</p>
                <span style="display: inline-block; padding: 0.35rem 0.75rem; background: rgba(99, 102, 241, 0.1); color: #818cf8; border-radius: 6px; font-size: 0.8rem; font-weight: 500;">Model: nvidia/Nemotron-3.5-Super-VL</span>
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

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<p style='text-align: center; color: #4b5563; font-size: 0.8rem;'>SOVEREIGN VAULT // PRIVACY-PRESERVING COGNITIVE GUARDIAN & LOAD-SHEDDING ENGINE</p>", unsafe_allow_html=True)
