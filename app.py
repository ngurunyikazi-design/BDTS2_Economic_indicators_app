import streamlit as st
import joblib
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Tanzania Stock Index Predictor",
    page_icon="📈",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #0d6efd;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #084298;
        color: white;
    }
    .prediction-box {
        background-color: #e9f5ff;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        color: #0d6efd;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
model = joblib.load("best_model.pkl")

# ---------------- TITLE ----------------
st.title("📊 Tanzania Stock Index Prediction App")
st.markdown("Predict stock index values based on key economic indicators.")

# ---------------- SIDEBAR ----------------
st.sidebar.header("📌 About")
st.sidebar.write("""
This app predicts Tanzania's stock index using:
- GDP Growth
- Inflation Rate
- Unemployment Rate
- Interest Rate
- Exchange Rate
""")

st.sidebar.info("Built with Streamlit & Machine Learning")

# ---------------- INPUT SECTION ----------------
st.subheader("Enter Economic Indicators")

col1, col2 = st.columns(2)

with col1:
    gdp = st.number_input("GDP Growth (%)", value=6.0)
    inflation = st.number_input("Inflation Rate (%)", value=4.0)
    unemployment = st.number_input("Unemployment Rate (%)", value=10.0)

with col2:
    interest = st.number_input("Interest Rate (%)", value=12.0)
    exchange = st.number_input("Exchange Rate (TZS)", value=2500.0)

# ---------------- PREDICTION ----------------
if st.button("Predict Stock Index"):
    features = np.array([[gdp, inflation, unemployment, interest, exchange]])
    prediction = model.predict(features)

    st.markdown(
        f"<div class='prediction-box'>Predicted Stock Index: {prediction[0]:.2f}</div>",
        unsafe_allow_html=True
    )

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("© 2026 Tanzania Economic AI Analytics Platform")

