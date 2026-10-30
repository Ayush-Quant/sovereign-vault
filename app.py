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
    page_title="Sovereign Vault | 3D Biometric Cognitive Monitor",
    page_icon="🛡️",
    layout="wide"
)

# --- 3D LIGHT-MODE BIOMETRIC DESIGN SYSTEM ---
st.markdown("""
<style>
    .stApp {
        background-color: #F8FAFC;
        color: #0F172A;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .biometric-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.25rem 1.75rem;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.04), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
        margin-bottom: 2rem;
    }
    .brand-title {
        font-size: 1.25rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        color: #0F172A;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    .live-badge {
        background-color: #ECFDF5;
        color: #059669;
        border: 1px solid #A7F3D0;
        padding: 0.3rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .alert-badge {
        background-color: #FEF2F2;
        color: #DC2626;
        border: 1px solid #FECACA;
        padding: 0.3rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .bio-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 18px;
        padding: 1.75rem;
        margin-bottom: 1.25rem;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    }
    .bio-card-critical {
        background: linear-gradient(145deg, #FFFFFF 0%, #FEF2F2 100%);
        border: 1px solid #FCA5A5;
        border-radius: 18px;
        padding: 1.75rem;
        margin-bottom: 1.25rem;
        box-shadow: 0 20px 25px -5px rgba(239, 68, 68, 0.08), 0 10px 10px -5px rgba(239, 68, 68, 0.04);
    }
    .process-pill-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 0.75rem;
        margin-bottom: 0.75rem;
    }
    .process-pill {
        background: #EEF2FF;
        color: #4F46E5;
        border: 1px solid #C7D2FE;
        padding: 0.35rem 0.85rem;
        border-radius: 8px;
        font-size: 0.8rem;
        font-family: monospace;
        font-weight: 600;
        box-shadow: 0 2px 4px rgba(79, 70, 229, 0.05);
    }
    .stButton>button {
        background: linear-gradient(135deg, #4F46E5 0%, #6366F1 100%) !important;
        color: #FFFFFF !important;
        font-weight: 600;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        box-shadow: 0 10px 20px -5px rgba(79, 70, 229, 0.4);
        transition: all 0.2s ease;
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #4338CA 0%, #4F46E5 100%) !important;
        box-shadow: 0 15px 25px -5px rgba(79, 70, 229, 0.6);
        transform: translateY(-2px);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #E2E8F0;
        padding: 6px;
        border-radius: 14px;
        border: 1px solid #CBD5E1;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        background-color: transparent;
        padding: 10px 20px;
    }
    .stTabs [data-baseweb="tab"] p {
        color: #0F172A !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FFFFFF !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08) !important;
    }
    .stTabs [aria-selected="true"] p {
        color: #4F46E5 !important;
    }
    label {
        color: #0F172A !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

init_db()

st.markdown("""
<div class="biometric-header">
    <div class="brand-title">
        <span>🛡️</span> SOVEREIGN VAULT <span style="font-size: 0.75rem; font-weight: 400; color: #64748B;">// 3D LIGHT COGNITIVE MONITOR</span>
    </div>
    <div>
        <span class="live-badge">● PERIMETER SECURE</span>
    </div>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["⚡ Live Telemetry & ECG", "🌐 Population Matrix", "📋 Feedback Vault"])

with tab1:
    st.sidebar.markdown("### 🎛️ Telemetry Calibration")
    st.sidebar.markdown("Adjust working memory strain parameters.")
    simulated_entropy = st.sidebar.slider("Cognitive Entropy Index", 0.0, 1.0, 0.85, 0.05)
    
    st.sidebar.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    st.sidebar.markdown("### 🔍 Active Process Context")
    app_input = st.sidebar.text_area("Currently Active Windows/Tabs", "Antigravity, MS Word, Slack, Browser Tabs (x14)")
    
    apps_list = [app.strip() for app in app_input.split(",") if app.strip()]

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("### 📈 Brain Entropy Vital Stream")
        
        if simulated_entropy > 0.7:
            st.markdown(f"""
            <div class="bio-card-critical">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 700; color: #DC2626; font-size: 0.85rem; letter-spacing: 0.05em;">STATE: ATTENTION RESIDUE OVERLOAD</span>
                    <span class="alert-badge">Critical Risk</span>
                </div>
                <div style="font-size: 3.5rem; font-weight: 800; color: #0F172A; margin: 0.5rem 0; letter-spacing: -0.03em;">
                    {simulated_entropy * 100:.0f}<span style="font-size: 1.5rem; color: #DC2626; font-weight: 600;">%</span>
                </div>
                <p style="color: #475569; font-size: 0.9rem; margin: 0;">High context-switching frequency detected. Estimated cognitive penalty: ~23 minutes per switch.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="bio-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 700; color: #059669; font-size: 0.85rem; letter-spacing: 0.05em;">STATE: DEEP FOCUS BASELINE</span>
                    <span class="live-badge">Optimal</span>
                </div>
                <div style="font-size: 3.5rem; font-weight: 800; color: #0F172A; margin: 0.5rem 0; letter-spacing: -0.03em;">
                    {simulated_entropy * 100:.0f}<span style="font-size: 1.5rem; color: #059669; font-weight: 600;">%</span>
                </div>
                <p style="color: #475569; font-size: 0.9rem; margin: 0;">Working memory perimeter secure. Friction levels within safe tolerance.</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("#### 🔗 Active Friction Sources")
        pills_html = "".join([f'<span class="process-pill">{app}</span>' for app in apps_list])
        st.markdown(f'<div class="process-pill-container">{pills_html}</div>', unsafe_allow_html=True)

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        
        chart_data = pd.DataFrame({
            "Time Window": [f"T-{i}" for i in range(10, 0, -1)],
            "Entropy Index": [0.2, 0.3, 0.35, 0.45, 0.55, 0.65, 0.7, 0.8, 0.82, simulated_entropy]
        })
        st.line_chart(chart_data, x="Time Window", y="Entropy Index", color="#4F46E5")

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
                        <span style="color: #DC2626; font-size: 1.2rem;">🛡️</span>
                        <strong style="color: #0F172A; letter-spacing: 0.05em; font-size: 0.95rem;">GUARDIAN INTERVENTION DIRECTIVE</strong>
                    </div>
                    <div style="color: #1E293B; font-size: 0.95rem; line-height: 1.7; white-space: pre-wrap; font-family: monospace;">{guardian_response}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="bio-card" style="text-align: center; padding: 3rem 1.5rem;">
                <div style="font-size: 2.5rem; margin-bottom: 1rem;">🛡️</div>
                <p style="color: #64748B; font-size: 0.95rem; margin-bottom: 1.5rem;">System on standby. Trigger the interceptor to evaluate telemetry and receive your tailored load-shedding directive.</p>
                <span style="display: inline-block; padding: 0.4rem 0.85rem; background: #EEF2FF; color: #4F46E5; border-radius: 8px; font-size: 0.8rem; font-weight: 600; border: 1px solid #C7D2FE;">Engine: nvidia/Nemotron-3.5-Super-VL</span>
            </div>
            """, unsafe_allow_html=True)
with tab2:
    st.markdown("### Team Stress Dashboard (100 Profiles)")
    st.markdown("Evaluating team well-being and stress levels across different professional roles.")
    
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
        df_cohort = df_cohort.rename(columns={
            "persona_id": "ID",
            "role": "Role",
            "context_switch_rate": "Task Switching Rate",
            "simulated_entropy": "Stress Score",
            "status": "Status"
        })
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Total People Evaluated", len(df_cohort))
        c2.metric("Balanced & Healthy", len(df_cohort[df_cohort["Status"] == "Balanced"]))
        c3.metric("Burnout Risks Flagged", len(df_cohort[df_cohort["Status"] == "Burnout Risk"]))
        
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        st.markdown("#### Member Details Breakdown")
        st.dataframe(df_cohort, height=400)
    else:
        st.warning("No simulation telemetry detected. Click 'Re-run Simulation Matrix' above.")
with tab3:
    st.markdown("### 📋 User Feedback & Telemetry Log")
    st.markdown("Submit your testing feedback directly into our secure Google Sheets vault.")
    
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="bio-card">', unsafe_allow_html=True)
        st.markdown("<h4 style='color: #0F172A; margin-bottom: 1.5rem;'>🔒 Secure Telemetry Submission Portal</h4>", unsafe_allow_html=True)
        
        with st.form("feedback_form"):
            col_l1, col_r1 = st.columns([1, 3])
            with col_l1:
                st.markdown("<p style='font-weight: 700; color: #0F172A; padding-top: 12px;'>Your Name</p>", unsafe_allow_html=True)
            with col_r1:
                fb_name = st.text_input("Name Input", label_visibility="collapsed", placeholder="Enter your full name...")
                
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
            
            col_l2, col_r2 = st.columns([1, 3])
            with col_l2:
                st.markdown("<p style='font-weight: 700; color: #0F172A; padding-top: 12px;'>Email Address</p>", unsafe_allow_html=True)
            with col_r2:
                fb_email = st.text_input("Email Input", label_visibility="collapsed", placeholder="Enter your email address...")
                
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
            
            col_l3, col_r3 = st.columns([1, 3])
            with col_l3:
                st.markdown("<p style='font-weight: 700; color: #0F172A; padding-top: 12px;'>Feedback / Notes</p>", unsafe_allow_html=True)
            with col_r3:
                fb_feedback = st.text_area("Feedback Input", label_visibility="collapsed", placeholder="Share your experience with the Socratic Guardian...")
                
            st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
            submitted = st.form_submit_button("Submit Feedback to Google Sheets")

            if submitted:
                if fb_name and fb_email and fb_feedback:
                    WEB_APP_URL = "https://script.google.com/macros/s/AKfycbxKxTU2MNdOsCkXSSxu6ha_Grlfl7Cr0tmb3hfBKwGtm-iOTRo3DveLfzhiksZR5Ycl/exec"
                    
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
        
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748B; font-size: 0.8rem;'>SOVEREIGN VAULT // 3D BIOMETRIC COGNITIVE GUARD & LOAD-SHEDDING ENGINE</p>", unsafe_allow_html=True)
