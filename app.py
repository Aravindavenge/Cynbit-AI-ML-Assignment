
import streamlit as st
import pandas as pd
import joblib
import os

# ==========================================
# TENANTEASE AI - MAIN APPLICATION
# ==========================================

st.set_page_config(
    page_title="TenantEase AI",
    page_icon="🏠",
    layout="wide"
)

# ==========================================
# LOAD MACHINE LEARNING MODEL
# ==========================================

MODEL_PATH = "models/rent_risk_model.pkl"
FEATURE_PATH = "models/features.pkl"
DATA_PATH = "data/tenant_payments.csv"

if not os.path.exists(MODEL_PATH):
    st.error("Model not found. Run model_training.py first.")
    st.stop()

if not os.path.exists(FEATURE_PATH):
    st.error("Feature file not found.")
    st.stop()

if not os.path.exists(DATA_PATH):
    st.error("Tenant dataset not found.")
    st.stop()

model = joblib.load(MODEL_PATH)
features = joblib.load(FEATURE_PATH)

# ==========================================
# HEADER
# ==========================================

st.title("🏠 TenantEase AI")

st.subheader(
    "Predictive Rent Risk & Intelligent Collection Assistant"
)

st.write(
    "An AI-powered property management assistant "
    "that analyses tenant payment history and "
    "predicts potential late-payment risks."
)

st.info(
    "Proof of Concept: This application uses "
    "synthetic tenant data for demonstration."
)

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv(DATA_PATH)

# ==========================================
# VALIDATE DATASET
# ==========================================

missing_columns = [
    column for column in features
    if column not in df.columns
]

if missing_columns:
    st.error(f"Missing dataset columns: {missing_columns}")
    st.stop()

# ==========================================
# PREDICT TENANT RISKS
# ==========================================

probabilities = model.predict_proba(
    df[features]
)[:, 1]

# ==========================================
# CLASSIFY TENANT RISK
# ==========================================

def classify_risk(probability):

    if probability >= 0.65:
        return "High Risk"

    elif probability >= 0.35:
        return "Medium Risk"

    else:
        return "Low Risk"


risk_categories = [
    classify_risk(p) for p in probabilities
]

high_risk = risk_categories.count("High Risk")
medium_risk = risk_categories.count("Medium Risk")
low_risk = risk_categories.count("Low Risk")

# ==========================================
# DASHBOARD OVERVIEW
# ==========================================

st.divider()

st.header("📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Tenants",
    len(df)
)

col2.metric(
    "High Risk",
    high_risk
)

col3.metric(
    "Medium Risk",
    medium_risk
)

col4.metric(
    "Low Risk",
    low_risk
)

# ==========================================
# RISK DISTRIBUTION CHART
# ==========================================

st.divider()

st.header("📈 Tenant Risk Distribution")

risk_data = pd.DataFrame({
    "Risk Category": [
        "Low Risk",
        "Medium Risk",
        "High Risk"
    ],

    "Number of Tenants": [
        low_risk,
        medium_risk,
        high_risk
    ]
})

st.bar_chart(
    risk_data.set_index("Risk Category")
)

# ==========================================
# TENANT RISK REPORT
# ==========================================

st.divider()

st.header("📋 Tenant Risk Report")

risk_report = df.copy()

risk_report["late_payment_probability"] = (
    probabilities * 100
).round(2)

risk_report["risk_category"] = risk_categories

st.write(
    "View predicted late-payment probabilities "
    "and risk categories for all tenants."
)

# Risk category filter
selected_risk = st.selectbox(
    "Filter tenants by risk",
    [
        "All",
        "High Risk",
        "Medium Risk",
        "Low Risk"
    ]
)

if selected_risk == "All":

    filtered_report = risk_report

else:

    filtered_report = risk_report[
        risk_report["risk_category"] == selected_risk
    ]

st.dataframe(
    filtered_report,
    use_container_width=True,
    hide_index=True
)

st.write(
    f"Showing {len(filtered_report)} tenant records."
)

# ==========================================
# DOWNLOAD TENANT RISK REPORT
# ==========================================

csv_data = risk_report.to_csv(index=False)

st.download_button(
    label="📥 Download Complete Tenant Risk Report",
    data=csv_data,
    file_name="tenant_risk_report.csv",
    mime="text/csv",
    use_container_width=True
)

# ==========================================
# INDIVIDUAL TENANT PREDICTION
# ==========================================

st.divider()

st.header("🔍 Individual Tenant Risk Prediction")

st.write(
    "Enter tenant payment information to predict "
    "the possibility of late rent payment next month."
)

with st.form("prediction_form"):

    tenant_id = st.text_input(
        "Tenant ID",
        value="TENANT_NEW_001"
    )

    col1, col2 = st.columns(2)

    with col1:

        late_payment_count = st.number_input(
            "Previous Late Payments",
            min_value=0,
            max_value=50,
            value=2
        )

        average_delay_days = st.number_input(
            "Average Payment Delay (Days)",
            min_value=0.0,
            max_value=365.0,
            value=7.0
        )

        outstanding_balance = st.number_input(
            "Outstanding Balance (₹)",
            min_value=0,
            max_value=1000000,
            value=2000
        )

    with col2:

        missed_payments = st.number_input(
            "Missed Payments",
            min_value=0,
            max_value=50,
            value=1
        )

        on_time_payment_rate = st.slider(
            "On-Time Payment Rate (%)",
            min_value=0.0,
            max_value=100.0,
            value=75.0
        )

    submitted = st.form_submit_button(
        "🔮 Predict Tenant Risk",
        use_container_width=True
    )

# ==========================================
# DISPLAY PREDICTION RESULTS
# ==========================================

if submitted:

    if not tenant_id.strip():

        st.error("Please enter a Tenant ID.")

    else:

        input_data = pd.DataFrame(
            [[
                late_payment_count,
                average_delay_days,
                outstanding_balance,
                missed_payments,
                on_time_payment_rate
            ]],
            columns=features
        )

        prediction_probability = model.predict_proba(
            input_data
        )[0][1]

        risk_percentage = prediction_probability * 100

        st.divider()

        st.header("🎯 Prediction Results")

        col1, col2 = st.columns(2)

        col1.metric(
            "Late Payment Probability",
            f"{risk_percentage:.2f}%"
        )

        if prediction_probability >= 0.65:

            risk_category = "HIGH RISK"

            col2.metric(
                "Risk Classification",
                risk_category
            )

            st.error("⚠️ High Risk Tenant")

            recommendation = (
                "Send a polite payment reminder before "
                "the due date. Contact the tenant to "
                "understand possible payment difficulties."
            )

        elif prediction_probability >= 0.35:

            risk_category = "MEDIUM RISK"

            col2.metric(
                "Risk Classification",
                risk_category
            )

            st.warning("⚠️ Medium Risk Tenant")

            recommendation = (
                "Monitor payment activity and send "
                "a friendly reminder before the due date."
            )

        else:

            risk_category = "LOW RISK"

            col2.metric(
                "Risk Classification",
                risk_category
            )

            st.success("✅ Low Risk Tenant")

            recommendation = (
                "Continue normal payment monitoring "
                "and appreciate the tenant's good "
                "payment history."
            )

        st.progress(
            float(prediction_probability)
        )

        # ==================================
        # RECOMMENDED ACTION
        # ==================================

        st.subheader("💡 Recommended Action")

        st.info(recommendation)

        # ==================================
        # FEATURE IMPORTANCE
        # ==================================

        st.subheader("📌 Important Model Factors")

        importance = pd.DataFrame({
            "Feature": features,
            "Importance": model.feature_importances_
        }).sort_values(
            by="Importance",
            ascending=False
        )

        st.bar_chart(
            importance.set_index("Feature")
        )

        st.caption(
            "Feature importance represents the overall "
            "influence of each variable in the trained model. "
            "It does not explain the exact reason for an "
            "individual prediction."
        )

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "TenantEase AI | Experimental AI/ML Proof of Concept "
    "| Python | Pandas | Scikit-learn | Streamlit"
)

st.caption(
    "Predictions are experimental and based on synthetic "
    "data. They should not be used as the sole basis "
    "for tenant-related decisions."
)
