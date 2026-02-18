import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("best_model.pkl")

st.title("Tanzania Stock Index Prediction App")

gdp = st.number_input("GDP Growth (%)")
inflation = st.number_input("Inflation Rate (%)")
unemployment = st.number_input("Unemployment Rate (%)")
interest = st.number_input("Interest Rate (%)")
exchange = st.number_input("Exchange Rate (TZS)")

if st.button("Predict Stock Index"):
    features = np.array([[gdp, inflation, unemployment, interest, exchange]])
    prediction = model.predict(features)
    st.success(f"Predicted Stock Index: {prediction[0]:.2f}")
