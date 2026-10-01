import streamlit as st
import pandas as pd
import joblib

# Load trained model once


@st.cache_resource
def load_model():
    return joblib.load("model.pkl")


model = load_model()


def dashboard_body():
    st.header("🔧 Property Repair Cost Estimation")

    st.write("Use the controls below to estimate repair cost based on job details.")

    # --- Dropdowns ---
    component = st.selectbox(
        "Component",
        ["windows", "plumbing", "roof", "electrics", "boiler"]
    )

    job_scope = st.selectbox(
        "Job Scope",
        ["minor", "moderate", "major"]
    )

    # --- Sliders ---
    component_age_years = st.slider(
        "Component Age (years)",
        min_value=0,
        max_value=60,
        value=10
    )

    inspection_score = st.slider(
        "Inspection Score",
        min_value=0,
        max_value=100,
        value=50
    )

    contractor_hours = st.slider(
        "Contractor Hours",
        min_value=0.0,
        max_value=100.0,
        value=3.0,
        step=0.5
    )

    # --- Prediction Button ---
    if st.button("Predict Repair Cost"):
        row = pd.DataFrame([{
            "component": component,
            "job_scope": job_scope,
            "component_age_years": component_age_years,
            "inspection_score": inspection_score,
            "contractor_hours": contractor_hours
        }])

        prediction = model.predict(row)[0]

        st.success(f"Estimated repair cost: £{prediction:,.2f}")
